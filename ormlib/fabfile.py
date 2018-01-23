#coding:utf-8
import fabric
from fabric.api import *

env.hosts = ['10.200.8.106']
env.user = 'oracle'
env.password = 'oracle'

def h():
	run('tail -f /var/log/messages')