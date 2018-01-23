#coding:utf-8
from django.contrib import admin
# Register your models here.
from demo.models import *



class BookInline(admin.TabularInline):
	model = Book



class AuthorAdmin(admin.ModelAdmin):
	inlines = [
		BookInline,
	]

class queueuserInline(admin.StackedInline):
	model = queueuser
	extra = 1

class syncqueueAdmin(admin.ModelAdmin):
	inlines = (queueuserInline,)
	# filter_horizontal = ('rqusers',)



admin.site.register(Author,AuthorAdmin)
admin.site.register(syncqueue,syncqueueAdmin)