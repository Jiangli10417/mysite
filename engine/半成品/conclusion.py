#!/usr/bin/python
#-*- coding:utf-8 -*-from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template, Context
from django.template import RequestContext
from django.shortcuts  import render_to_response
from django.utils import simplejson
from django.db.models import Q
from models import Bill,Account,Templet863,Templetac863,Templetall863,Project,Login,User,Asset,Asset_Type
import datetime
import string

def con_f_select(request):
    pro=Account.objects.all()
    return render_to_response("con_select_f.html",locals()) 
    
def con_y_select(request):
    pro=Account.objects.all()
    return render_to_response("con_select_y.html",locals()) 
    
def con_t_select(request):
    pro=Account.objects.all()
    return render_to_response("con_select_t.html",locals()) 
    
def con_f_show(request):
    pid=request.POST["acid"]
    resulthigh=Bill.objects.filter(proid=pid).filter(money_gte=100000)
    resultlow=Bill.objects.filter(proid=pid).filter(money_lt=100000)
    acc=Account.objects.get(project_id=pid)
    return render_to_response("con_finish.html",locals(),context_instance = RequestContext(request))
    
def con_y_show(request):
    pid=request.POST["acid"]
    resulthigh=Bill.objects.filter(proid=pid).filter(money_gte=100000)
    resultlow=Bill.objects.filter(proid=pid).filter(money_lt=100000)
    acc=Account.objects.get(project_id=pid)
    return render_to_response("con_year.html",locals(),context_instance = RequestContext(request))
    
def con_t_show(request):
    pid=request.POST["acid"]
    resulthigh=Bill.objects.filter(proid=pid).filter(money_gte=100000)
    resultlow=Bill.objects.filter(proid=pid).filter(money_lt=100000)
    acc=Account.objects.get(project_id=pid)
    return render_to_response("con_timing.html",locals(),context_instance = RequestContext(request))
    
    
