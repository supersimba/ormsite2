#coding:utf-8

from django.contrib import admin

from ormapp.models import *

admin.site.site_url='/ormindex/'
admin.site.site_header='ORACLE同步监控管理'


class QueueRelationUserInline(admin.TabularInline):
    model = QueueRelationUser
    extra = 1


class RepQueueAdmin(admin.ModelAdmin):
    filter_horizontal=('rqusers',)
    inlines = (QueueRelationUserInline,)
    list_display = ['describe','src_ip','src_path','src_ssh_user','src_ssh_pwd','src_dbid',
                    'dbps_port','extract_port','tgt_ip','tgt_path','tgt_ssh_user','tgt_ssh_pwd',
                    'tgt_dbid','collect_port','src_script_path','tgt_script_path']

    fieldsets = (
        (
          None,{
              'fields':('describe',)
          }
        ),
        ('源端：',
         {
             'fields':('src_ip','src_path','src_ssh_user','src_ssh_pwd','src_dbid','dbps_port','extract_port','src_script_path')
         }
        ),
        ('目标端：',
         {
             'fields': ('tgt_ip','tgt_path','tgt_ssh_user','tgt_ssh_pwd','tgt_dbid','collect_port','tgt_script_path')
         }
        ),
    )

admin.site.register(rep_queue,RepQueueAdmin)