#!/usr/bin/python
#-*-coding:utf-8-*-
from django.contrib import admin
from models import Bill,Account,Project,User,Kindname,Protemplate,Kindcontent,Prokindaccount,Tempname,Billchange_record,Accountadd_record,Billdevice_record,User_history


admin.site.register(Bill)
admin.site.register(Account)
admin.site.register(Project)
admin.site.register(User)
admin.site.register(User_history)
admin.site.register(Kindname)
admin.site.register(Protemplate)
admin.site.register(Kindcontent)
admin.site.register(Prokindaccount)
admin.site.register(Tempname)
admin.site.register(Billchange_record)
admin.site.register(Accountadd_record)
admin.site.register(Billdevice_record)
