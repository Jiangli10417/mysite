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

def showpro(request):
    pro_id=request.GET["id"]
    probj = Bill.objects.filter(proid=pro_id).order_by("time")
    obj=Project.objects.get(pid=pro_id)
    acc=Account.objects.get( project_id=pro_id)
    sum1=acc.money_sum
    kind=obj.prokind
    if (obj.prokind=="863"):
        tem=Templetcost863.objects.get(temp_id=pro_id)
        a1=tem.device_cost
        a2=tem.material_cost
        a3=tem.test_cost
        a4=tem.fuel_cost
        a5=tem.trip_cost
        a6=tem.meeting_cost
        a7=tem.coperation_cost
        a8=tem.publish_cost
        a9=tem.labor_cost
        a0=tem.other_cost
        a1=(a1/sum1)*100
        a2=(a2/sum1)*100
        a3=(a3/sum1)*100
        a4=(a4/sum1)*100
        a5=(a5/sum1)*100
        a6=(a6/sum1)*100
        a7=(a7/sum1)*100
        a8=(a8/sum1)*100
        a9=(a9/sum1)*100
        a0=(a0/sum1)*100
        other=100-(a1+a2+a3+a4+a5+a6+a7+a8+a9+a0)
    if (obj.prokind=="自然基金"):
        tem=TempletcostNature.objects.get(temp_id=pro_id)
        a1=tem.device_cost
        a2=tem.data_cost
        a3=tem.consult_cost
        a4=tem.print_cost
        a5=tem.trip_cost
        a6=tem.meeting_cost
        a7=tem.coperation_cost
        a8=tem.info_cost
        a9=tem.labor_cost
        a0=tem.other_cost
        a1=(a1/sum1)*100
        a2=(a2/sum1)*100
        a3=(a3/sum1)*100
        a4=(a4/sum1)*100
        a5=(a5/sum1)*100
        a6=(a6/sum1)*100
        a7=(a7/sum1)*100
        a8=(a8/sum1)*100
        a9=(a9/sum1)*100
        a0=(a0/sum1)*100
        other=100-(a1+a2+a3+a4+a5+a6+a7+a8+a9+a0)
    return render_to_response("showprodata.html",locals(),context_instance = RequestContext(request))
    
