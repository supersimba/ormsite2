# coding:utf-8
# 检查ssh连通性,及目录是否存在,文件是否存在
import sys
import paramiko
import os
from ormlogger import Logger
import time


while True:
    print 'begin to connect'
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cli.connect('10.200.8.106', 22, 'oracle', 'oracle',allow_agent=False,look_for_keys=False,timeout=5)
        print 'connection OK!!!!!!!!!!!!!!'
    except Exception as e:
        # ssh 联通失败
        print e
        print 'connection failed ...'
    finally:
        cli.close()
    # time.sleep(1)