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


def search(request):
    acc=Account.objects.all().order_by("project_id")
    return render_to_response("spendsearch.html",locals())
    
def spendshow(request):
    startime = request.POST["starttime"]
    entime = request.POST["endtime"]
    acid = request.POST["accid"]
    if acid=="全部":
        result = Bill.objects.filter(time__lte=entime).filter(time__gte=startime)
    result = Bill.objects.filter(proid=acid).filter(time__lte=entime).filter(time__gte=startime)
    return render_to_response("spendshow.html",locals(),context_instance = RequestContext(request))
    
def spend_all(request):
    return render_to_response("pro_chose.html")

#def spendall_show(request):
#    kind=request.POST[acckind]
#    if kind=='863':
#        cost=Templet863.objects.all().order_by("temp_id")
#        acc=Templetall863.objects.all().order_by("temp_id")
#        return render_to_response("show863.html",locals(),context_instance = RequestContext(request))
#    if kind=='自然基金':
#    return
    
