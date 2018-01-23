#coding:utf-8
#源端同步信息采集调度器
from apscheduler.schedulers.blocking import *
import MySQLdb
import logging
import paramiko
import datetime
import time
from checkconfig import check_remote
import ConfigParser
from ormlogger import Logger




def get_src_queue(dbip,dbport,dbuser,dbpwd,dbname):
    hd.info('exec function --- get_src_queue')
    rows=()
    try:
        # hd.info('connect to database')
        db = MySQLdb.connect(host=dbip, port=dbport, user=dbuser, passwd=dbpwd, db=dbname)
        # db = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='simba2017', db='ormdb')
        hd.info('success connect to database')
        c = db.cursor()
        c.execute("select rid,src_ip,src_path,src_ssh_user,src_ssh_pwd,src_script_path from rep_queue order by rid")
        rows = c.fetchall()
        hd.info("get %d records." %(len(rows)))
    except Exception, e:
        hd.error(e)
    finally:
        return rows
        db.close()


# def get_src_moni_info():
#     hd.info('exec function -- get_src_moni_info')
#     args = get_src_queue(dbip,int(dbport),dbuser,dbpwd,dbname)
#     if len(args) > 0 :
#         # 有需要检查的队列记录
#         print args

#     else:
#         # 没有需要检查的队列记录
#         hd.info('queue record if empty , continue cycle')



if __name__ == "__main__":
    while True:
        logger = Logger('ttt', '../log/t.log')
        hd = logger.logger_addhandler()
        hd.info('TTTTTTTTTTTTTTTTTTT :%s' %(str(datetime.datetime.now())))
        time.sleep(1)
        logger.closed()