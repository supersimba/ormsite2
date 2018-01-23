# coding:utf-8
# 检查ssh连通性,及目录是否存在,文件是否存在
import sys
import paramiko
import os
from ormlogger import Logger


def check_remote(sship, sshuser, sshpwd, softpath, scriptpath):
    lger = Logger('chkconfig', '../log/collectsrcschd.log')
    logger = lger.logger_addhandler()
    logger.info('exec function ----- check_remote')
    logger.info('begin to check %s:%s and scriptpath %s' %
                (sship, softpath, scriptpath))
    dir_list = [softpath, scriptpath]
    # 检查列表内容顺序：ssh检查  软件目录检查  脚本检查
    chk_list = []
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        cli.connect(sship, 22, sshuser, sshpwd)
        logger.info('success connect to %s' % (sship))
        chk_list.append(1)
        logger.info('check %s and %s' % (softpath, scriptpath))
        if len(dir_list) == 2:
            for l in dir_list:
                stdin, stdout, stderr = cli.exec_command("ls -rld " + l)
                err = stderr.readlines()
                if len(err) > 0:
                    logger.warning('failed to check %s' % (l))
                    chk_list.append(-1)
                else:
                    logger.info('success to check %s' % (l))
                    chk_list.append(1)
            return chk_list
    except:
        # ssh 联通失败
        logger.warning('failed to connect to %s' % (sship))
        return [-1, -1, -1]
    finally:
        cli.close()
        lger.closed()
