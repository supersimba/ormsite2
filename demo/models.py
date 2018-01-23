#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
import datetime



class Author(models.Model):
   name = models.CharField(max_length=100)
   class Meta:
        db_table='author'
        verbose_name=u'作者'
        verbose_name_plural=verbose_name


class Book(models.Model):
   author = models.ForeignKey(Author)
   title = models.CharField(max_length=100)
   class Meta:
        db_table='book'
        verbose_name=u'著作'
        verbose_name_plural=verbose_name


class syncqueue(models.Model):
    sid=models.AutoField(primary_key=True)
    describe=models.CharField(max_length=100,blank=False,verbose_name=u'队列描述')
    ip=models.GenericIPAddressField(blank=False,verbose_name=u'源端IP')
    path=models.CharField(max_length=100,blank=False,verbose_name=u'源端路径')
    # rqusers=models.ManyToManyField(User,verbose_name=u'可监控用户')
    rqusers = models.ManyToManyField(User,verbose_name=u'可监控用户',through='queueuser')

    class Meta:
        db_table='syncqueue'
        verbose_name=u'队列配置表'
        verbose_name_plural=verbose_name


class queueuser(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    rep_queue_sid = models.ForeignKey(syncqueue)

    class Meta:
        db_table='queueuser'
        verbose_name=u'队列用户多对多关系表'
        verbose_name_plural=verbose_name