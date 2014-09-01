#encoding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template, Context
from django.template import RequestContext
from django.shortcuts  import render_to_response
from django.utils import simplejson
from django.db.models import Q
from models import Bill,Account,Project,User,Kindname,Protemplate,Kindcontent,Prokindaccount,Tempname
import datetime
import string

def login(request):
    return render_to_response("login.html")

def logincheck(request):
        try:
            name = request.POST["uname"]
            pwd = request.POST["upwd"]
        except:
            return render_to_response( "login.html",{'nameerror':'非法'})
        try:
            obj = User.objects.get(uid = name)
        except:
            return render_to_response( "login.html",{'nameerror':'账户不存在'})
        if pwd == obj.password:
            request.session["Uid"]=name
            request.session["Upwd"]=pwd
            person_show=name
            if obj.permission == u'财务':
                return render_to_response( "financial.html",locals())
            if obj.permission == u'负责人':
                return render_to_response( "responsible.html",locals())
            if obj.permission == u'管理员':
                return render_to_response( "manager.html",locals())
            if obj.permission == 'system':
                return render_to_response( "systemuser.html",locals())
            return render_to_response( "login.html",{'nameerror':'没有进入权限'})
        return render_to_response( "login.html",{'pwderror':'密码错误'})

def logout(request):
    del request.session["Uid"]
    del request.session["Upwd"]
    return render_to_response("login.html")

