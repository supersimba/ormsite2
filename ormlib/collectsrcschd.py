# coding:utf-8
# 源端同步信息采集调度器
from apscheduler.schedulers.blocking import *
import MySQLdb
import logging
import paramiko
import datetime
from checkconfig import check_remote
import ConfigParser
import threading
import time

from ormlogger import Logger
import checkconfig
from mysqldbhelper import MySqlUtil


def get_src_queue(dbip, dbport, dbuser, dbpwd, dbname):
    #hd.info('exec function -- get_src_queue')
    rows = ()
    try:
        # hd.info('connect to database')
        db = MySQLdb.connect(host=dbip, port=dbport,
                             user=dbuser, passwd=dbpwd, db=dbname)
        c = db.cursor()
        c.execute(
            "select src_ip,src_path,src_ssh_user,src_ssh_pwd,src_script_path,rid from rep_queue order by rid")
        rows = c.fetchall()
        #hd.info("get %d records." % (len(rows)))
    except Exception, e:
        hd.error(e)
    finally:
        return rows
        db.close()


def get_src_sync_info(cls):
    hd.info('exec function --- get_src_sync_info')
    for l in cls:
        srcip = l[0]
        srcpath = l[1]
        sshuser = l[2]
        sshpwd = l[3]
        scriptpath = l[4]
        check_list = check_remote(srcip, sshuser, sshpwd, srcpath, scriptpath)
        ssh_status = check_list[0]
        path_status = check_list[1]
        script_status = check_list[2]
        # print type(ssh_status),type(path_status),type(script_status)
        if check_list[0] == 1 and check_list[1] == 1 and check_list[2] == 1:
            # 全部为1检查通过,否则不进行数据采集
            hd.info('begin to collect sync information from %s:%s' %
                    (str(srcip), str(srcpath)))
            cli = paramiko.SSHClient()
            cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                cli.connect(srcip, 22, sshuser, sshpwd)
                stdin, stdout, stderr = cli.exec_command("sh " + scriptpath + " "+srcpath)
                out = stdout.readlines()
                err = stderr.readlines()
                if out:
                    dbobj = MySqlUtil(host=dbip, user=dbuser,pwd=dbpwd, dbname=dbname, port=int(dbport))
                    sql = "insert into src_moni_info(src_ssh_status,src_path_status,exec_script_status,dbps_cnt,capture_cnt,sender_cnt,sync_status,active,capture_err,sender_err,queue_id_id,add_time) values(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s')" %(ssh_status, path_status, script_status, int(out[0].strip("\n")), int(out[1].strip("\n")), int(out[2].strip("\n")), int(out[3].strip("\n")), int(out[4].strip("\n")), int(out[5].strip("\n")), int(out[6].strip("\n")),int(l[5]),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    dbobj.exec_insert(sql)
            except Exception as e:
                hd.warning(e)
            finally:
                cli.close()
        else:
            # 检查未通过,不进行数据采集
            hd.info('failed check connection or softdir or scriptpath')
            dbobj=MySqlUtil(host = dbip, user = dbuser, pwd = dbpwd,
                              dbname = dbname, port = int(dbport))
            sql="insert into src_moni_info(src_ssh_status,src_path_status,exec_script_status,queue_id_id,add_time) values(%d,%d,%d,%d,'%s')" % (
                ssh_status, path_status, script_status, int(l[5]), datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            dbobj.exec_insert(sql)

if __name__ == "__main__":
    cf=ConfigParser.ConfigParser()
    cf.read('../ormconfig.ini')
    dbip=cf.get('mysql_connection', 'host')
    dbport=cf.get('mysql_connection', 'port')
    dbuser=cf.get('mysql_connection', 'user')
    dbpwd=cf.get('mysql_connection', 'pwd')
    dbname=cf.get('mysql_connection', 'dbname')
    # 开启的thread 数量
    thrdnum=int(cf.get('schd', 'thrdnum'))
    frequency=int(cf.get('schd', 'frequency'))
    
    

    while True:
        #hd.info('begin to collect source dsg information............................')
        l=Logger('collectsrcschd', '../log/collectsrcschd.log')
        hd=l.logger_addhandler()
        record_list=get_src_queue(dbip, int(dbport), dbuser, dbpwd, dbname)
        hd.info('ready to alloc job queue, threads :%d ,records:%d' %
                (thrdnum, len(record_list)))
        thd_list=[]
        job_list=[]
        for j in range(1, thrdnum + 1):
            job_list.append([])
        # print job_list
        if len(record_list) == 0:
            # 无记录，继续循环
            hd.info('records is 0 ,continue to cycle')
            pass
        else:
            # if len(record_list) <= thrdnum and len(record_list) > 0:
            # 记录数>0,为每个thread分配记录，最后按分配的job_list进行多线程开启
            flag=0
            for n in record_list:
                job_list[flag].append(n)
                flag += 1
                if flag == thrdnum:
                    flag=0
            #hd.info('complete alloc job queue , alloc open threads')

            for jl in job_list:
                if len(jl) > 0:
                    t=threading.Thread(
                        target = get_src_sync_info, args = (jl,))
                    thd_list.append(t)

            for t in thd_list:
                t.setDaemon(False)
                t.start()

            for j in thd_list:
                j.join()

        hd.info('-----------------------------------------------------complete job -----------------------------------------------------')
        l.closed()
        time.sleep(frequency)
