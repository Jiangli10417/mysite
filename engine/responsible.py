#encoding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template, Context
from django.template import RequestContext
from django.shortcuts  import render_to_response
from django.utils import simplejson
from django.db.models import Q
from models import Bill,Account,Project,User,Kindname,Protemplate,Kindcontent,Prokindaccount,Tempname,Billchange_record,Accountadd_record,Billdevice_record
import datetime
import string
import time

def responsible_account(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    account_content = Account.objects.all()
    return render_to_response("responsible_account.html",locals())

def responsible_account_show(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    account_content = Account.objects.all()
    result = Bill.objects.all()
    if 'time' in request.POST:
        starttime = request.POST["starttime"]
        endtime = request.POST["endtime"]
        t1 = datetime.datetime.strptime(starttime, "%Y-%m-%d").date()
        t2 = datetime.datetime.strptime(endtime, "%Y-%m-%d").date()
        if t2 < t1:
            error="时间选择出错"
            return render_to_response("responsible_account.html",locals())
        result = result.filter(time__lte=endtime).filter(time__gte=starttime)
        proid = request.POST["proid"]

    if 'pid' in request.POST:
        print 1
        proid = request.POST["proid"]
        if proid != u'全部' and proid != '':
            print 2
            result = result.filter(proid=proid)
            kind_list = request.REQUEST.getlist("propaykind")
            if kind_list[0] != u'全部':
                for i in kind_list:
                    result = result.filter(paykind = i)
        if proid ==u'全部':
            kind_list = request.REQUEST.getlist("propaykind")
            if kind_list[0] != u'全部':
                for i in kind_list:
                    result = result.filter(paykind = i)
        if proid =='':
            error="请选择项目号"
            return render_to_response("responsible_account.html",locals())
    if 'money_ref' in request.POST:
        result = result.filter(money__gte = string.atof(request.POST["money"]))
    show = True
    for i in result:
        i.time = i.time.strftime('%Y-%m-%d')

    return render_to_response("responsible_account.html",locals())
    
###############################################################################################################

###############################################################################################################

def responsible_pro(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    d1 = datetime.datetime.now()
    d2 = d1 + datetime.timedelta(days = 90)
    pro_expire = Project.objects.filter(pEnd__lte = d2 , iscreate = True).order_by("pEnd")
    pro_unexpire = Project.objects.filter(pEnd__gt = d2 , iscreate = True).order_by("pEnd")
    proid_id_expire=[]
    proid_id_unexpire=[]


    for i in pro_expire:
        proid_id_expire.append(i.pid)
    for j in pro_unexpire:
        proid_id_unexpire.append(j.pid) 
    pro_expire_show = Account.objects.filter(project_id__in = proid_id_expire)
    pro_unexpire_show = Account.objects.filter(project_id__in = proid_id_unexpire)
    
    for k in pro_expire_show:
        k.money_act = round((k.money_cost/k.money_sum)*100 , 2 )
        k.money_cost = k.money_cost / 10000
        k.money_sum = k.money_sum / 10000
        tem = Project.objects.get(pid = k.project_id)
        k.account_id = tem.pEnd.strftime('%Y-%m-%d')

    for h in pro_unexpire_show:
        h.money_act = round((h.money_cost/h.money_sum)*100 , 2 )
        h.money_cost = h.money_cost / 10000
        h.money_sum = h.money_sum / 10000
        tem = Project.objects.get(pid = h.project_id)
        h.account_id = tem.pEnd.strftime('%Y-%m-%d')
       
    return render_to_response("responsible_pro.html",locals())
    
def responsible_pro_show(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    proid = request.GET["id"]
    pro_info = Project.objects.get(pid = request.GET["id"])
    account_kind = Prokindaccount.objects.filter(proid = proid)
    for i in account_kind:
        if i.money_sum == 0:
            i.buff = -1
        else:
            i.money_cost = i.money_cost / 10000
            i.money_sum = i.money_sum / 10000
            i.buff = round((i.money_cost/i.money_sum)*100,2)
    account_info = Account.objects.get(project_id = proid)
    

    cost_rate = round((account_info.money_cost/account_info.money_sum)*100,2)
    add_rate = round((account_info.money_act/account_info.money_sum)*100,2)
    account_info.money_sum = account_info.money_sum / 10000
    account_info.money_act = account_info.money_act / 10000
    result = Bill.objects.filter(proid = proid).order_by("time")
    return render_to_response("responsible_pro_show.html",locals())
    
def responsible_pro_show_kind(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    proid = request.GET["pid"]
    kind = request.GET["id"]
    obj = Account.objects.get(project_id = proid)
    moneyall = obj.money_sum/10000
    kind_account = Prokindaccount.objects.get(proid = proid,payname=kind)
    bill_obj = Bill.objects.filter(proid = proid , paykind = kind)
    kind_account.money_cost = kind_account.money_cost / 10000
    kind_account.money_sum = kind_account.money_sum / 10000
    
    return render_to_response("responsible_pro_show_kind.html",locals())
###############################################################################################################################

###############################################################################################################################

def responsible_all(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    account_obj = Account.objects.all()
    cost1=0
    act1=0
    sum1 = 0
    for i in account_obj:
        sum1 = sum1+i.money_sum/10000
        cost1 = cost1+i.money_cost/10000
        act1 = act1+i.money_act/10000
    cost_rate_all = round((cost1/sum1)*100 , 2)
    act_rate_all = round((act1/sum1)*100,2)
    sum2 = sum1
    kind_all = Tempname.objects.all()
    list_kind = []
    kindname = Kindname.objects.all()
    for i in kindname:
        list_kind.append(i.name)
    kindDict = dict.fromkeys(list_kind, "")
    
    count_sum = 0
    count_cost = 0
    sstr = ""
    for i in list_kind:
        acobj = Prokindaccount.objects.filter(payname = i)
        for j in acobj:
            count_sum = count_sum + j.money_sum/10000
            count_cost = count_cost + j.money_cost/10000
        
        
        sstr =str(count_sum) + "/" + str(count_cost)
        kindDict[i]=sstr
        count_cost=0
        count_sum=0
    return render_to_response("responsible_all.html",locals())
    
def responsible_all_kindshow(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    kind=request.GET["id"]
    sum1=request.GET["s"]
    proid_obj=Project.objects.filter(prokind = kind , iscreate = True)
    if proid_obj:
        sum_kind=0.0
        act_kind=0.0
        cost_kind=0.0
        for i in proid_obj:
            a=Account.objects.get(project_id = i.pid)
            sum_kind = sum_kind + a.money_sum
            act_kind = act_kind + a.money_act
            cost_kind =cost_kind + a.money_cost
        sum_kind_rate = round((float(sum_kind)/float(sum1))/100,2)
        act_kind_rate = round((act_kind/sum_kind)*100,2)
        cost_kind_rate = round((cost_kind/sum_kind)*100,2)
        kindname=[]
        kindcost=[]
        kindsum=[]
        kind_obj=Protemplate.objects.filter(prokind = kind).order_by("payname")
        for i in kind_obj:
            kindname.append(i.payname)
        k=0
        cost=0
        sum3=0
        print kindname
        for j in kindname:
            for i in proid_obj:
                obj1 = Prokindaccount.objects.get(proid = i.pid,payname = j)
                cost=cost+obj1.money_cost
                sum3=sum3+obj1.money_sum
                k=k+1
            kindcost.append(cost)
            kindsum.append(sum3)
            k=0
            cost=0
            sum3=0
        k=0
        print kindcost
        for i in kind_obj:
            i.buff_one=round((kindcost[k]/sum_kind)*100,2)
            i.buff_two=round((kindsum[k]/sum_kind)*100,2)
            i.buff_three = kindcost[k]/10000
            i.buff_four = kindsum[k]/10000
            k=k+1
            print i.buff_one
            print i.buff_two
        sum_kind = sum_kind/10000
        act_kind = act_kind/10000
        cost_kind = cost_kind/10000
        return render_to_response("responsible_all_kindshow.html",locals())
    else:
        return render_to_response("responsible_all_kindshow.html",locals())
    
###########################################################################################

###########################################################################################
def responsible_account_finish(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    profinish = Project.objects.filter(pEnd__lte = datetime.datetime.now() , iscreate =True)
    print profinish
    return render_to_response("responsible_account_finish.html",locals())

def responsible_account_finish_show(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    profinish = Project.objects.filter(pEnd__lte = datetime.datetime.now())
    try:
        proid = request.POST["proid"]
        
        account_obj = Account.objects.get(project_id = proid)
        
        account_obj.money_sum = account_obj.money_sum/10000
        account_obj.money_cost = account_obj.money_cost/10000
        
        account_add_obj = Accountadd_record.objects.filter(project_id = proid)
        for f in account_add_obj:
            f.money_add = f.money_add/10000
        
        bill_obj = Bill.objects.filter(proid = proid)
        kind_account_obj = Prokindaccount.objects.filter(proid = proid)
        for k in kind_account_obj:
            k.buff = (k.money_sum-k.money_cost)/10000
            k.money_sum = k.money_sum/10000
            k.money_cost=k.money_cost/10000
        pro_obj = Project.objects.get(pid = proid)
        pro_obj.pEnd = pro_obj.pEnd.strftime('%Y-%m-%d')
        pro_obj.pStart = pro_obj.pStart.strftime('%Y-%m-%d')
        prokind = pro_obj.prokind
        kind_obj = Protemplate.objects.filter( prokind =prokind )
        device_obj = Billdevice_record.objects.filter(proid = proid)
        num = 0
        #num_obj = Kindcontent.objects.filter(id = 1)
        dataList = []
    
        for i in kind_obj:
            a = Kindcontent.objects.filter(name = i.payname)
            for j in a:
                dataList.append(j.content)
            
        dataDict = dict.fromkeys(dataList, 0)
        for i in dataList:
            b = device_obj.filter(name = i)
            for j in b:
                num = num + j.number
            dataDict[i] = num
            num = 0
    
    
        #b = device_obj.filter(paykind = i.payname)
        #for j in a:
        #    c = b.filter(name = j.content)
       #     for h in c:
        #        num = num + h.number
         #   j.number = num
        #    num = 0

    #num_obj.order_by("name")
        show = True
        return render_to_response("responsible_account_finish.html",locals())
    except:
        error='项目号为空'
        return render_to_response("responsible_account_finish.html",locals())
########################################################################################

########################################################################################
def responsible_account_year(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    pro_obj = Project.objects.filter(pEnd__gte = datetime.datetime.now() , iscreate = True)
    return render_to_response("responsible_account_year.html",locals())

def responsible_account_year_show(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    year = request.POST["time"]
    proid = request.POST["proid"]
    year1 = year + '-12-31'
    year2 = year + '-01-01'
    t1 = datetime.datetime.strptime(year1, "%Y-%m-%d").date()
    t2 = datetime.datetime.strptime(year2, "%Y-%m-%d").date()

    
    pro_obj = Project.objects.filter(pEnd__gte = datetime.datetime.now())

    pro = Project.objects.get(pid = proid)
    if pro.pStart > t1 or pro.pEnd < t2:
        error = '时间错误'
        return render_to_response("responsible_account_year.html",locals())
    pro.pEnd = pro.pEnd.strftime('%Y-%m-%d')
    pro.pStart = pro.pStart.strftime('%Y-%m-%d')
    bill_obj = Bill.objects.filter(time__year = year , proid = proid)
    ID = []
    for i in bill_obj:
        ID.append(i.id)
    device_obj = Billdevice_record.objects.filter(Bill_sqlid__in = ID)
    account_add = Accountadd_record.objects.filter(project_id = proid , time__year = year)
    
    for f in account_add:
        f.time = f.time.strftime('%Y-%m-%d')
        f.money_add = f.money_add/10000
    
    account_obj = Account.objects.get(project_id = proid)
    account_obj.money_sum = account_obj.money_sum/10000
    account_obj.money_cost = account_obj.money_cost/10000
    kind_account_obj = Prokindaccount.objects.filter(proid = proid)
    for k in kind_account_obj:
        k.buff = (k.money_sum-k.money_cost)/10000
        k.money_sum = k.money_sum/10000
        k.money_cost=k.money_cost/10000
    kind_obj = Protemplate.objects.filter( prokind = pro.prokind )
    num = 0
    dataList = []
    for i in kind_obj:
        dataList.append(i.payname)
    dataDict_kind = dict.fromkeys(dataList, 0)
    for i in dataList:
        a = bill_obj.filter(paykind = i)
        for j in a:
            num = num +j.money
        dataDict_kind[i] = num/10000
        num = 0
        
    List=[]
    for i in kind_obj:
        a = Kindcontent.objects.filter(name = i.payname)
        for j in a:
            List.append(j.content)
            
    dataDict_device = dict.fromkeys(List, 0)
    for i in List:
        b = device_obj.filter(name = i)
        for j in b:
            num = num + j.number
        dataDict_device[i] = num
        num = 0
    show = True
    return render_to_response("responsible_account_year.html",locals())
    
##########################################################################################

##########################################################################################

def responsible_billchange_record(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    pro = Account.objects.all()
    return render_to_response("responsible_billchange_record.html",locals())
    
def responsible_billchange_record_show(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    proid = request.POST["proid"]
    if proid == u'全部':
        bill_chenge = Billchange_record.objects.all()
    else:
        bill_chenge = Billchange_record.objects.filter(proid = proid)
    show = True
    return render_to_response("responsible_billchange_record.html",locals())
