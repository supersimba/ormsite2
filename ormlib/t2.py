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
import threading


def func():
    hd.info('exec func'+threading.currentThread().getName())
    print hd
    #logger.closed()


if __name__ == "__main__":
    while True:
        logger = Logger('t', '../log/t2.log')
        hd = logger.logger_addhandler()
        l=[]
        for i in range(1,6):
            t=threading.Thread(target=func)
            l.append(t)

        for t in l:
            t.setDaemon(False)
            t.start()

        for j in l:
            j.join()

        logger.closed()
        time.sleep(2)