# coding:utf-8
# 目标端同步信息采集调度器
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


def get_tgt_queue(dbip, dbport, dbuser, dbpwd, dbname):
    rows = ()
    try:
        db = MySQLdb.connect(host=dbip, port=dbport,
                             user=dbuser, passwd=dbpwd, db=dbname)
        c = db.cursor()
        c.execute(
            "select tgt_ip,tgt_path,tgt_ssh_user,tgt_ssh_pwd,tgt_script_path,rid from rep_queue order by rid")
        rows = c.fetchall()
    except Exception, e:
        hd.error(e)
    finally:
        return rows
        db.close()


def get_tgt_sync_info(cls):
    hd.info('exec function --- get_tgt_sync_info')
    for l in cls:
        tgtip = l[0]
        tgtpath = l[1]
        sshuser = l[2]
        sshpwd = l[3]
        scriptpath = l[4]
        check_list = check_remote(tgtip, sshuser, sshpwd, tgtpath, scriptpath)
        ssh_status = check_list[0]
        path_status = check_list[1]
        script_status = check_list[2]
        # print type(ssh_status),type(path_status),type(script_status)
        if check_list[0] == 1 and check_list[1] == 1 and check_list[2] == 1:
            #print 'check is ok ok ok'
            cli = paramiko.SSHClient()
            # 全部为1检查通过,否则不进行数据采集
            cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                cli.connect(tgtip, 22, sshuser, sshpwd)
                stdin, stdout, stderr = cli.exec_command("sh " + scriptpath + " "+tgtpath)
                out = stdout.readlines()
                err = stderr.readlines()
                print out
                if out:
                    # print l[5],type(l[5]),out[6],type(int(out[0])),type(int(out[1])),type(int(out[2])),type(int(out[3])),type(int(out[4])),type(int(out[5])),type(int(out[6]))
                    dbobj = MySqlUtil(host=dbip, user=dbuser,pwd=dbpwd, dbname=dbname, port=int(dbport))
                    sql = "insert into tgt_moni_info(tgt_ssh_status,tgt_path_status,exec_script_status,sync_status,active,collect_cnt,collect_err,loader_s_cnt,loader_r_cnt,loader_s_p_cnt,loader_r_p_cnt,loader_rate,loader_time,loader_err,queue_id,add_time) values(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,'%s','%s','%s',%d,'%s')" %(ssh_status, path_status, script_status, int(out[10].strip("\n")),int(out[8].strip("\n")),int(out[0].strip("\n")),int(out[1]),int(out[2]),int(out[3]),int(out[4]),int(out[5].strip("\n")),str(out[9].strip("\n")),str(out[6].strip("\n")),str(out[7].strip("\n")),int(l[5]),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    print sql
                    dbobj.exec_insert(sql)
            except Exception as e:
                hd.warning(e)
            finally:
                cli.close()
        else:
            # 检查未通过,不进行数据采集
            hd.info('failed check target host connection or softdir or scriptpath')
            dbobj=MySqlUtil(host = dbip, user = dbuser, pwd = dbpwd,
                              dbname = dbname, port = int(dbport))
            sql="insert into tgt_moni_info(tgt_ssh_status,tgt_path_status,exec_script_status,queue_id,add_time) values(%d,%d,%d,%d,'%s')" % (
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
        # hd.info('begin to collect source dsg information............................')
        l=Logger('collecttgtschd', '../log/collecttgtschd.log')
        hd=l.logger_addhandler()
        record_list=get_tgt_queue(dbip, int(dbport), dbuser, dbpwd, dbname)
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
            # hd.info('complete alloc job queue , alloc open threads')

            for jl in job_list:
                if len(jl) > 0:
                    t=threading.Thread(
                        target = get_tgt_sync_info, args = (jl,))
                    thd_list.append(t)

            for t in thd_list:
                t.setDaemon(False)
                t.start()

            for j in thd_list:
                j.join()

        hd.info('-----------------------------------------------------complete job -----------------------------------------------------')
        l.closed()
        time.sleep(frequency)
