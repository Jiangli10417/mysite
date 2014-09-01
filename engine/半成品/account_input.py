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

def input_search(request):
    return render_to_response("input_search.html")  


def cost_input(request):
    try:
        if request.method == 'POST':
            pro = Project.objects.get(pid = request.POST["projectid"])
            if(pro.iscreate==True):            
                kind = pro.prokind
                project=request.POST["projectid"]
                pronum= request.POST["projectid"]
                user=User.objects.filter(permission='财务')
                return render_to_response("account_input.html",locals(),context_instance = RequestContext(request))
            return render_to_response("input_search.html",{'error':'无此帐号'},context_instance = RequestContext(request))     
    except:
        return render_to_response("input_search.html",{'error':'数据库异常'},context_instance = RequestContext(request))  

def input_continue(request):
    try:
        accid=request.GET["accid"]
        cokind=request.GET["cokind"]
        time=request.GET["time"]
        name=request.GET["name"]
        money=string.atof(request.GET["money"])
        person=request.GET["person"]
        pnum=request.GET["pnum"]
        note=request.GET["note"]
        p=Project.objects.get(pid=accid)
        
        billobj=Bill(time=time, name=name, money=money,transactor=person,bill_id=pnum,paykind=cokind,proid=accid,note=note)
        
        billobj.save()
        print p.prokind
        if p.prokind=='863':
            a = Templetcost863.objects.get(temp_id = accid)
            if cokind==u'设备费':
                b = a.device_cost+money
                a.device_cost=b
            if cokind==u'材料费':
                b = a.material_cost+money
                a.material_cost=b
            if cokind==u'测试费':
                b = a.test_cost+money
                a.test_cost=b
            if cokind==u'燃料费':
                b = a.fuel_cost+money
                a.fuel_cost=b
            if cokind==u'差旅费':
                b = a.trip_cost+money
                a.trip_cost=b
            if cokind==u'会议费':
                b = a.meeting_cost+money
                a.meeting_cost=b
            if cokind==u'国际合作交流费':
                b = a.coperation_cost+money
                a.coperation_cost=b
            if cokind==u'出版文献等':
                b = a.publish_cost+money
                a.publish_cost=b
            if cokind==u'劳务费':
                b = a.labor_cost+money
                a.labor_cost=b
            if cokind==u'其他费用':
                b = a.other_cost+money
                a.other_cost=b
        if p.prokind==u'自然基金':
            a = TempletcostNature.objects.get(temp_id = accid)
            if cokind==u'设备费':
                b = a.device_cost+money
                a.device_cost=b
            if cokind==u'数据采集费':
                b = a.data_cost+money
                a.data_cost=b
            if cokind==u'专家咨询费':
                b = a.consult_cost+money
                a.consult_cost=b
            if cokind==u'印刷费':
                b = a.print_cost+money
                a.print_cost=b
            if cokind==u'差旅费':
                b = a.trip_cost+money
                a.trip_cost=b
            if cokind==u'会议费':
                b = a.meeting_cost+money
                a.meeting_cost=b
            if cokind==u'国际合作交流费':
                b = a.coperation_cost+money
                a.coperation_cost=b
            if cokind==u'资料费':
                b = a.info_cost+money
                a.info_cost=b
            if cokind==u'劳务费':
                b = a.labor_cost+money
                a.labor_cost=b
            if cokind==u'其他费用':
                b = a.other_cost+money
                a.other_cost=b
            a.save()
        c = Account.objects.get(project_id = accid)
        b = c.money_lef - money
        c.money_lef = b
        c.save()
        
        alldata=[]
        onedata = [0,0]
        onedata[0] = "1"
        onedata[1] = '2'
        alldata.append(onedata)
        json = simplejson.dumps(alldata)
        return HttpResponse(json, 'application/javascript')
    except:
        return render_to_response("input_search.html",{'error':'网页出错请联系工作人员'},context_instance = RequestContext(request))  
def input_finish(request):
    try:
        #if request.method == 'POST':
        accid=request.POST["projectnum"]
        cokind=request.POST["costkind"]
        time=request.POST["time"]
        name=request.POST["name"]
        money=string.atof(request.POST["money"])
        person=request.POST["person"]
        pnum=request.POST["pnum"]
        note=request.POST["note"]
        p=Project.objects.get(pid=accid)
        
        billobj=Bill(time=time, name=name, money=money,transactor=person,bill_id=pnum,paykind=cokind,proid=accid)
        
        billobj.save()
        if p.prokind=='863':
            a = Templetcost863.objects.get(temp_id = accid)
            if cokind==u'设备费':
                b = a.device_cost+money
                a.device_cost=b
            if cokind==u'材料费':
                b = a.material_cost+money
                a.material_cost=b
            if cokind==u'测试费':
                b = a.test_cost+money
                a.test_cost=b
            if cokind==u'燃料费':
                b = a.fuel_cost+money
                a.fuel_cost=b
            if cokind==u'差旅费':
                b = a.trip_cost+money
                a.trip_cost=b
            if cokind==u'会议费':
                b = a.meeting_cost+money
                a.meeting_cost=b
            if cokind==u'国际合作交流费':
                b = a.coperation_cost+money
                a.coperation_cost=b
            if cokind==u'出版文献等':
                b = a.publish_cost+money
                a.publish_cost=b
            if cokind==u'劳务费':
                b = a.labor_cost+money
                a.labor_cost=b
            if cokind==u'其他费用':
                b = a.other_cost+money
                a.other_cost=b
        if p.prokind==u'自然基金':
            a = TempletcostNature.objects.get(temp_id = accid)
            if cokind==u'设备费':
                b = a.device_cost+money
                a.device_cost=b
            if cokind==u'数据采集费':
                b = a.data_cost+money
                a.data_cost=b
            if cokind==u'专家咨询费':
                b = a.consult_cost+money
                a.consult_cost=b
            if cokind==u'印刷费':
                b = a.print_cost+money
                a.print_cost=b
            if cokind==u'差旅费':
                b = a.trip_cost+money
                a.trip_cost=b
            if cokind==u'会议费':
                b = a.meeting_cost+money
                a.meeting_cost=b
            if cokind==u'国际合作交流费':
                b = a.coperation_cost+money
                a.coperation_cost=b
            if cokind==u'资料费':
                b = a.info_cost+money
                a.info_cost=b
            if cokind==u'劳务费':
                b = a.labor_cost+money
                a.labor_cost=b
            if cokind==u'其他费用':
                b = a.other_cost+money
                a.other_cost=b
            a.save()
        c = Account.objects.get(project_id = accid)
        b = c.money_lef - money
        c.money_lef = b
        c.save()
        return render_to_response("input_search.html",{'error':'录入成功'},context_instance = RequestContext(request)) 
    except:
        return render_to_response("input_search.html",{'error':'错误'},context_instance = RequestContext(request)) 
        
def add_search(request):
    return render_to_response("addsearch.html")  
    
def money_add(request):
    try:
       
        pro=Project.objects.get(pid = request.POST["projectid"])
        proinfo=Account.objects.get(project_id=request.POST["projectid"])
        
        if (pro.iscreate==True):
            if (pro.prokind=="863"):
                pro_id=pro.pid
                proid=pro_id
                cost=Templetcost863.objects.get(temp_id = pro_id)
                acall=Templetall863.objects.get(temp_id = pro_id)
                a1=(cost.device_cost/acall.device_cost)*100
                a2=(cost.material_cost/acall.material_cost)*100
                a3=(cost.test_cost/acall.test_cost)*100
                a4=(cost.fuel_cost/acall.fuel_cost)*100
                a5=(cost.trip_cost/acall.trip_cost)*100
                a6=(cost.meeting_cost/acall.meeting_cost)*100
                a7=(cost.coperation_cost/acall.coperation_cost)*100
                a8=(cost.publish_cost/acall.publish_cost)*100
                a9=(cost.labor_cost/acall.labor_cost)*100
                a0=(cost.other_cost/acall.labor_cost)*100
                
                return render_to_response("account_add863.html",locals(),context_instance = RequestContext(request))
            if (pro.prokind == u'自然基金'):
                pro_id=pro.pid
                proid=pro_id
                cost=TempletcostNature.objects.get(temp_id = pro_id)
                acall=TempletallNature.objects.get(temp_id = pro_id)
                a1=(cost.device_cost/acall.device_cost)*100
                a2=(cost.data_cost/acall.data_cost)*100
                a3=(cost.consult_cost/acall.consult_cost)*100
                a4=(cost.print_cost/acall.print_cost)*100
                a5=(cost.trip_cost/acall.trip_cost)*100
                a6=(cost.meeting_cost/acall.meeting_cost)*100
                a7=(cost.coperation_cost/acall.coperation_cost)*100
                a8=(cost.info_cost/acall.info_cost)*100
                a9=(cost.labor_cost/acall.labor_cost)*100
                a0=(cost.other_cost/acall.labor_cost)*100
                
                return render_to_response("account_addnature.html",locals(),context_instance = RequestContext(request))
        return render_to_response("addsearch.html",{'error':'查无此号'},context_instance = RequestContext(request))
    except:
        return render_to_response("addsearch.html",{'error':'网页出错请联系工作人员'},context_instance = RequestContext(request))

def result_check(request):
    try:
        proid = request.POST["proid"]
        acc=Account.objects.get(project_id=proid)
        a=acc.money_act
        b=acc.money_lef
        acc.money_act=a+string.atof(request.POST["money_add"])
        acc.money_lef=b+string.atof(request.POST["money_add"])
        acc.save()
        return render_to_response("addsearch.html",{'error':'录入成功'},context_instance = RequestContext(request))
    except:
        return render_to_response("addsearch.html",{'error':'数据库出错请联系工作人员'},context_instance = RequestContext(request))
    
    #acall=Templetall863.objects.get(project_id = proid)
    #acc=Templetac863.objects.get(project_id = proid)
    
   # check1 = accall.device_cost-acc.device_cost-device
    #check2 = accall.material_cost-acc.material_cost-material
    #check3 = accall.test_cost-acc.test_cost-test
    #check4 = accall.fuel_cost-acc.fuel_cost-fuel
    #check5 = accall.meeting_cost-acc.meeting_cost-meeting
    #check6 = accall.coperation_cost-acc.coperation_cost-coperation
    #check7 = accall.publish_cost-acc.publish_cost-publish
    #check8 = accall.labor_cost-acc.labor_cost-labor
    #check9 = accall.other_cost-acc.other_cost-other
    #check10 = accall.trip_cost-acc.trip_cost-trip
    
   # if()
 
 #   material_add
  #  test_add
   # fuel_add
   # trip_add
   # meeting_add
   # coperation_add
   # publish_add
   # labor_add
   # other_add  

 #class Bill(models.Model):                     #凭单表
   # time = models.DateTimeField(u'时间')
   # name = models.CharField(u'名称',max_length=50)
   # money = models.FloatField (u'单价')
    #number = models.IntegerField (u'数量')
    #transactor = models.ForeignKey('User')    #经办人：外键
  #  voucher_id = models.CharField(u'凭单号',max_length=50)
   # note = models.TextField(u'备注',max_length=300)
   # bill_id = models.CharField(u'票号',max_length=50,primary_key=True)
   # paykind = models.CharField(u'支出种类',max_length=50)
   # proid = models.CharField(u'项目号',max_length=50)
 

  
 
 
 
 
 
 
 
 
 
 
# def submitTypeEdition(request):
 #   assetType = request.GET["assetType"]
 #   description = request.GET["description"]
#    
 #   assetTypeObj = AssetType(asset_type = assetType,
#                            description = description)
 #   assetTypeObj.save()

#    alldata=[]
 #   onedata = [0,0]
  # onedata[0] = "1"
#onedata[1] = '2'
 #   alldata.append(onedata)
  # json = simplejson.dumps(alldata)
   # return HttpResponse(json, 'application/javascript')

