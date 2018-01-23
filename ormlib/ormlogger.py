#coding:utf-8
#logging 封装类
import sys
import logging
from logging.handlers import RotatingFileHandler



class Logger(object):
    def __init__(self, logger_name, filename):
        self.logger = ''
        self.handler = ''
        self.loggr_name = logger_name
        self.logfile = filename
        self.logger = logging.getLogger(logger_name)

    def logger_addhandler(self):
        self.logger.setLevel(logging.INFO)
        self.handler = RotatingFileHandler(self.logfile, maxBytes=150000000, backupCount=5)
        fmter = logging.Formatter('%(asctime)s %(name)s<%(levelno)s>: %(message)s')
        self.handler.setFormatter(fmter)
        self.logger.addHandler(self.handler)
        return self.logger

    def closed(self):
        self.handler.close()
        self.logger.removeHandler(self.handler)


ll=Logger('aaa','111')

