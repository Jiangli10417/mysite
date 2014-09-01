#encoding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template, Context
from django.template import RequestContext
from django.shortcuts  import render_to_response
from django.utils import simplejson
from django.db.models import Q
from models import Bill,Account,Templetcost863,Templetall863,TempletallNature,TempletcostNature,Project,Login,User,Asset,Asset_Type
import datetime
import string

def welcom(request):
    showprof = Account.objects.filter(money_lef__lte=0).order_by("money_lef")
    showprot = Account.objects.filter(money_lef__gt=0).order_by("money_lef")
    for row in showprot:
        row.money_act = (row.money_lef/row.money_sum)*100
        
    return render_to_response("index.html",locals())
