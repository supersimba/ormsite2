#coding:utf-8
#mysql操作类
import MySQLdb
import logging
import datetime
import ConfigParser
from ormlogger import Logger



class MySqlUtil(object):
	def __init__(self,host,user,pwd,dbname,port):
		self.host = host
		self.port = port
		self.user = user
		self.pwd = pwd
		self.dbname = dbname
		try:
			self.conn = MySQLdb.connect(self.host,self.user,self.pwd,self.dbname,self.port)
			self.cursor = self.conn.cursor()
		except Exception as e:
			print 'connection or cursor create failed,%s' %(e)
		finally:
			pass
		#self.conn = MySQLdb.connect(self.host,self.user,self.pwd,self.dbname,self.port)


	def exec_insert(self,sqlstr):
		#print sqlstr
		try:
			self.cursor.execute(sqlstr)
			self.conn.commit()
		except Exception as e:
			print e
			self.conn.rollback()
		finally:
			self.close_conn()


	def exec_query(self,sqlstr):
		try:
			self.cursor.execute(sqlstr)
		except Exception as e:
			print e
		finally:
			return self.cursor.fetchall()
			close_conn()

	def close_conn(self):
		self.conn.close()
		
		



# mydb = MySqlUtil('127.0.0.1','root','simba2017','ormdb',3306)
# print mydb.exec_query("select count(*) from rep_queue")