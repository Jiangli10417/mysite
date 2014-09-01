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

def create_search(request):
    return render_to_response("create_search.html")
    
def create_proshow(request):
    try:
        if request.method == 'POST':
            try:
                pro=Project.objects.get(pid = request.POST["projectid"])
                
                if pro.iscreate == False:                
                    projectid = pro.pid
                    proname = pro.pName            
                    promang = pro.pManager 
                    procon = pro.pConntent
                   
                 #   prostr = pro.pStart
                  #  proend = pro.End
                  #  print pro.End
            
                    return render_to_response("showproject.html",locals(),context_instance = RequestContext(request))    
                return render_to_response("create_search.html",{'error':'已存在帐号'},context_instance = RequestContext(request))
            except:
                return render_to_response("create_search.html",{'error':'项目号不存在'},context_instance = RequestContext(request))
    except: 
        return render_to_response("create_search.html",{'error':'网页出错'},context_instance = RequestContext(request))   

def create(request):
    #try:                             
        pro=Project.objects.get(pid = request.GET["id"])
        if pro.prokind == '863':
            return render_to_response("create_863.html",{'pro':pro},context_instance = RequestContext(request))
        if pro.prokind == u'自然基金':
            return render_to_response("create_nature.html",{'pro':pro},context_instance = RequestContext(request))
        #return render_to_response("create_search.html",{'error':'数据库出错请联系工作人员'},context_instance = RequestContext(request))      
    #except: 
        #return render_to_response("create_search.html",{'error':'网页出错请联系工作人员'},context_instance = RequestContext(request))   
        
def create_success(request):
    try:
        if request.method == 'POST':  
            try:
                
                d1=Project.objects.get(pid=request.POST["proid"])         
                if(d1.prokind=='863'):
                    p = Templetall863(
                    temp_id = d1,       
                    device_cost = string.atof(request.POST["device"]),
                    material_cost = string.atof(request.POST["material"]),
                    test_cost = string.atof(request.POST["test"]),
                    fuel_cost = string.atof(request.POST["fuel"]),
                    trip_cost = string.atof(request.POST["trip"]),
                    meeting_cost = string.atof(request.POST["meeting"]),
                    coperation_cost = string.atof(request.POST["coperation"]),
                    publish_cost = string.atof(request.POST["publish"]),
                    labor_cost = string.atof(request.POST["labor"]),
                    other_cost = string.atof(request.POST["other"]),
                    )
                    p.save()
                
                    a = Account(  
                    project_id = d1, 
                    money_sum = string.atof(request.POST["moneyall"]),
                    money_act = string.atof(request.POST["moneyac"]),
                    money_lef = string.atof(request.POST["moneyac"]),
                    )
                    a.save()
               
                    c = Templetcost863(
                    temp_id = d1,       
                    device_cost = 0.00,
                    material_cost = 0.00,
                    test_cost = 0.00,
                    fuel_cost = 0.00,
                    trip_cost = 0.00,
                    meeting_cost = 0.00,
                    coperation_cost = 0.00,
                    publish_cost = 0.00,
                    labor_cost = 0.00,
                    other_cost = 0.00,
                
                    )
                    c.save()
                    accountid=request.POST["proid"]
                    d1.iscreate=True
                    d1.save()
                    return render_to_response("create_success.html",locals(),context_instance = RequestContext(request)) 
                if(d1.prokind==u'自然基金'):
                    p = TempletallNature(
                    temp_id = d1,       
                    device_cost = string.atof(request.POST["device"]),
                    data_cost = string.atof(request.POST["data"]),
                    consult_cost = string.atof(request.POST["consult"]),
                    print_cost = string.atof(request.POST["print"]),
                    trip_cost = string.atof(request.POST["trip"]),
                    meeting_cost = string.atof(request.POST["meeting"]),
                    coperation_cost = string.atof(request.POST["coperation"]),
                    info_cost = string.atof(request.POST["info"]),
                    labor_cost = string.atof(request.POST["labor"]),
                    other_cost = string.atof(request.POST["other"]),
                    )
                    p.save()
                
                    a = Account(  
                    project_id = d1, 
                    money_sum = string.atof(request.POST["moneyall"]),
                    money_act = string.atof(request.POST["moneyac"]),
                    money_lef = string.atof(request.POST["moneyac"]),
                    )
                    a.save()
               
                    c = TempletcostNature(
                    temp_id = d1,       
                    device_cost = 0.00,
                    data_cost = 0.00,
                    consult_cost = 0.00,
                    print_cost = 0.00,
                    trip_cost = 0.00,
                    meeting_cost = 0.00,
                    coperation_cost = 0.00,
                    info_cost = 0.00,
                    labor_cost = 0.00,
                    other_cost = 0.00,
                
                    )
                    c.save()
                    accountid=request.POST["proid"]
                    d1.iscreate=True
                    d1.save()
                    return render_to_response("create_success.html",locals(),context_instance = RequestContext(request)) 
            except:
                return render_to_response("create_search.html",{'error':'数据库出错请联系工作人员'},context_instance = RequestContext(request)) 
        return render_to_response("create_search.html",{'error':'网页出错请联系工作人员'},context_instance = RequestContext(request)) 
    except:  
        return render_to_response("create_search.html",{'error':'网页出错请联系工作人员'},context_instance = RequestContext(request))               



  
#def result_check(request):
 #   errors = []
#    if request:
#        p_num = request.POST["pnum"],
#        check_error = Bill.objects.filter(bill_id = p_num)
#        if check_error:
#           return render_to_response("account_input.html",locals(),context_instance = RequestContext(request))                 
##        try:
  #          p=Bill(    proid = request.POST["project"],
   #                    time = request.POST["time"],
    #                   money =string.atof(request.POST["money"]),
       #                number = string.atoi(request.POST["num"]),
        #               note=request.POST["note"],
         #              bill_id=request.POST["pnum"],
          #             name=request.POST["name"],
 #                   )
  #          p.save()
   #     except:
    #         input_error=True
     #        return render_to_response("account_input.html",locals(),context_instance = RequestContext(request))
    #return render_to_response("account_input.html",locals(),context_instance = RequestContext(request))
    
#def account_addsearch(request):
 #   return render_to_response("account_addsearch.html")
    
#def account_add(reaquest):
 #   if request:
  #      pro=Project.objects.filter(pid = request.POST["projectid"])
   #     if (pro and pro.iscreate==True):
     #       if (pro.prokind=="863"):
    #            pro_id=pro.pid
#                cost=Templet863.objects.filter(project_id = pro_id)
 #               acall=Templetall863.objects.filter(project_id = pro_id)
  #              acc=Templetac863.objects.filter(project_id = pro_id)
#
 #               device_costtem = cost.device_cost                
  #              material_costtem = cost.material_cost
   #             test_costtem = cost.test_cost
    #            fuel_costtem = cost.fuel_cost
     #           trip_costtem = cost.trip_cost
      #          meeting_costtem = cost.meeting_cost
       #         coperation_costtem = cost.coperation_cost
        #        publish_costtem = cost.publish_cost
         #       labor_costtem = cost.labor_cost
          #      other_costtem = cost.other_cost
                
           #     device_costall = acall.device_cost                
            #    material_costall = acall.material_cost
#                test_costall = acall.test_cost
 #               fuel_costall = acall.fuel_cost
  #              trip_costall = acall.trip_cost
   #             meeting_costall = acall.meeting_cost
    #            coperation_costall = acall.coperation_cost
     #           publish_costall = acall.publish_cost
      #          labor_costall = acall.labor_cost
       #         other_costall = acall.other_cost
                
        #        device_costac = acc.device_cost                
         #       material_costac = acc.material_cost
          #      test_costac = acc.test_cost
           #     fuel_costac = acc.fuel_cost
            #    trip_costac = acc.trip_cost
             #   meeting_costac = acc.meeting_cost
              #  coperation_costac = acc.coperation_cost
               # publish_costac = acc.publish_cost
#                labor_costac = acc.labor_cost
#                other_costac = acc.other_cost
#                
 #               return render_to_response("account_addto863.html",locals(),context_instance = RequestContext(request))
  #      else:
            
   #         return render_to_response("account_addsearch.html",{'error':'查无此号'},context_instance = RequestContext(request))
  #  return render_to_response("account_addsearch.html",{'error':'网页出错请联系工作人员'},context_instance = RequestContext(request))
    

    

