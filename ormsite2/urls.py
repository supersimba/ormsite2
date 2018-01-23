#coding:utf-8
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView
from ormapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),


    url(r'^ormindex/$',ormindex),
    url(r'^orminfo/$',orminfo),
    url(r'^ormlogout/$',ormlogout),

    url(r'^display_source_info/$',display_source_info),
    url(r'^display_target_info/$',display_target_info),
    url(r'^ormlogs/(?P<rid>\d+)/(?P<logtype>[0-1])/$',ormlogs,name='show_ormlogs'),
    url(r'^check_process/$',check_process),
    url(r'^display_log/$',display_log),
]
