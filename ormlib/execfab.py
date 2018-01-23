#coding:utf-8
import fabric
from fabric.api import *
import subprocess

# while True:
p = subprocess.Popen("fab -f fabfile.py h")
p.wait()