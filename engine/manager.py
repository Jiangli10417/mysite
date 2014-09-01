#encoding=utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Template, Context
from django.template import RequestContext
from django.shortcuts  import render_to_response
from django.utils import simplejson
from django.db.models import Q
from models import Bill,Account,Project,User,Kindname,Protemplate,Kindcontent,Prokindaccount,Tempname,Billchange_record,Billdevice_record
import datetime
import string

def tempedit(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    tempn=Tempname.objects.all()
    kindn=Kindname.objects.all()
    
    return render_to_response( "Tempedit.html",locals())


def tempedit_add(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    tempname = request.POST["new"]
    try:
        a=Tempname.objects.get(kindname = tempname)
        print a
        error='模版已存在'
        tempn=Tempname.objects.all()
        kindn=Kindname.objects.all()
        return render_to_response( "Tempedit.html",locals())
    except:
        b=Tempname(kindname = tempname,)
        b.save()
        error='模版录入成功'
        tempn=Tempname.objects.all()
        kindn=Kindname.objects.all()
        return render_to_response( "Tempedit.html",locals())

def tempedit_showcontent(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    name = request.GET["name"]
    obj = Protemplate.objects.filter(prokind = name)
    i=[]
    for c in obj:
        i.append(c.payname)
    data = simplejson.dumps(i)
    return HttpResponse(data, 'application/javascript')

def tempedit_add_edit(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    name=request.GET["name"]
    content=request.GET["content"]
    Protemplate.objects.filter(prokind = name).delete()
    str1=content
    s = str1.split(',')
    print s
    for i  in range(0,len(s)-1):
        c=s[i]
        b=Protemplate( prokind = name, payname = c, )
        b.save()
    alldata=[]
    onedata = [0,0]
    onedata[0] = "1"
    onedata[1] = '2'
    alldata.append(onedata)
    data = simplejson.dumps(alldata)
    return HttpResponse(data, 'application/javascript')
    
def tempedit_del(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    try:
        name=request.POST["prodel_select"]
        print name
        if name!='':
            Protemplate.objects.filter(prokind = name).delete()
            Tempname.objects.filter(kindname=name).delete()
            tempn=Tempname.objects.all()
            kindn=Kindname.objects.all()
            error='删除成功'
            return render_to_response( "Tempedit.html",locals())
        else:
            tempn=Tempname.objects.all()
            kindn=Kindname.objects.all()
            error='错误'
            return render_to_response( "Tempedit.html",locals())
    except:
        tempn=Tempname.objects.all()
        kindn=Kindname.objects.all()
        error='请选择'
        return render_to_response( "Tempedit.html",locals())
############################################################################


#############################################################################
        
def kindconedit(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    kindn = Kindname.objects.all()
    
    return render_to_response( "kindconedit.html",locals())

def kindconedit_add(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    name=request.POST["new"]
    try:
        a=Kindname.objects.get(name = name)
        error='种类存在'
        kindn = Kindname.objects.all()
        return render_to_response( "kindconedit.html",locals())
    except:
        a=Kindname(name = name,)
        a.save()
        b=Kindcontent(name=name ,content = " ")
        kindn = Kindname.objects.all()
        return render_to_response( "kindconedit.html",locals())
        
        
def kindconedit_add_edit(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    name = request.GET["name"]
    content = request.GET["content"]
    Kindcontent.objects.filter(name = name).delete()
    str1=content
    print str1
    s = str1.split(',')
    print s
    for i  in range(0,len(s)-1):
        c=s[i]
        b=Kindcontent( name = name, content = c, )
        b.save()
    alldata=[]
    onedata = [0,0]
    onedata[0] = "1"
    onedata[1] = '2'
    alldata.append(onedata)
    data = simplejson.dumps(alldata)
    return HttpResponse(data, 'application/javascript')
    
def kindconedit_showcontent(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    k=request.GET["name"]
    obj = Kindcontent.objects.filter(name = k)
    i=[]
    for c in obj:
        i.append(c.content)
    data = simplejson.dumps(i)
    return HttpResponse(data, 'application/javascript')


def kindconedit_del(request):#ok
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    
    try:
        name = request.POST["kinddel_select"]
        Kindcontent.objects.filter(name=name).delete()
        Kindname.objects.get(name=name).delete()
        kindn = Kindname.objects.all()
        return render_to_response( "kindconedit.html",locals())
    except:
        error='出错,请选择'
        kindn = Kindname.objects.all()
        return render_to_response( "kindconedit.html",locals())

######################################################################

######################################################################

def accountinput_edit(request):#!
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    accountedit=Account.objects.all().order_by("project_id")
    return render_to_response("accountinput_edit.html",locals())

def accountinput_edit_show(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    accountedit=Account.objects.all().order_by("project_id")
    starttime = request.POST["starttime"]
    endtime = request.POST["endtime"]
    t1 = datetime.datetime.strptime(starttime, "%Y-%m-%d").date()
    t2 = datetime.datetime.strptime(endtime, "%Y-%m-%d").date()
    if t2<t1:
        error="时间选择出错"
        return render_to_response("accountinput_edit.html",locals())
    proid = request.POST["proid"]
    show = True
    if proid==u'全部':
        result = Bill.objects.filter(time__lte=endtime).filter(time__gte=starttime)
        return render_to_response("accountinput_edit.html",locals())
    else:
        result = Bill.objects.filter(proid=proid).filter(time__lte=endtime).filter(time__gte=starttime)
        return render_to_response("accountinput_edit.html",locals())
        
def accountinput_edit_check(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    bill_sql_id=request.POST["bill_sql_id"]
    flag=request.POST["flag"]
    bill_edit_show = Bill.objects.get(id = bill_sql_id)
    name = bill_edit_show.name
    name = name.replace(",", "")
    bill_edit_show.time = bill_edit_show.time.strftime('%Y-%m-%d')
    obj1 = Project.objects.get(pid = bill_edit_show.proid)
    obj2 = Account.objects.get(project_id = bill_edit_show.proid)
    acid =obj2.account_id
    kind = Protemplate.objects.filter(prokind = obj1.prokind)
    kindcontent = Billdevice_record.objects.filter(Bill_sqlid = bill_sql_id)
    for i in kindcontent:
        name = name.strip(i.name)
    if flag==u'更改':
        return render_to_response("accountinput_edit_edit.html",locals())
    if flag==u'删除':
        return render_to_response("accountinput_edit_del.html",locals())
        
def accountedit_kindcontent_show(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    kindname=request.GET["kind"]
    i=[]
    obj = Kindcontent.objects.filter(name = kindname)
    for c in obj:
        i.append(c.content)
    data = simplejson.dumps(i)
    return HttpResponse(data, 'application/javascript')

def accountinput_edit_submit(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    billid = request.POST["billid"]
    money = request.POST["money"]
    time = request.POST["time"]
    payname = request.POST["payname"]
    note = request.POST["note"]
    namecontent = request.POST["namecontent"]
    numbercontent = request.POST["numbercontent"]
    bill_sqlid = request.POST["bill_sqlid"]
    pwd = request.POST["pwd"]
    obj1 = Bill.objects.get(id = bill_sqlid)
    fini_person=obj1.transactor
    obj2 = User.objects.get(uid=fini_person)
    if obj2.password != pwd:
        error='密码不正确'
        accountedit=Account.objects.all().order_by("project_id")
        return render_to_response("accountinput_edit.html",locals())
    obj3=Prokindaccount.objects.get( proid = obj1.proid , payname = obj1.paykind )
    obj3.money_cost=obj3.money_cost - obj1.money
    obj3.save()
    
    obj6=Prokindaccount.objects.get( proid = obj1.proid , payname = payname )
    obj6.money_cost=obj6.money_cost + string.atof(money)
    obj6.save()
    
    obj4=Account.objects.get( project_id =obj1.proid )
    obj4.money_cost = obj4.money_cost - obj1.money + string.atof(money)
    
    obj4.save()
    obj5 = Billchange_record(transactor = obj1.transactor,billsql_id = obj1.id,time = datetime.datetime.now(),proid = obj1.proid,operation= u'修改',)
    obj5.save()
    obj1.money=string.atof(money)
    obj1.time = time
    obj1.note=note
    obj1.paykind=payname
    obj1.name=namecontent
    obj1.bill_id=billid
    obj1.change=True
    obj1.save()
    device_del = Billdevice_record.objects.filter(Bill_sqlid = bill_sqlid)
    device_del.delete()
    str1=namecontent
    str2=numbercontent
    s1 = str1.split(',')
    s2 = str2.split(',')
    for i  in range(0,len(s2)-1):
        bsave = Billdevice_record(Bill_sqlid = obj1.id, proid = obj1.proid,name = s1[i],number = string.atof(s2[i]),paykind = payname,)
        bsave.save()
    error='修改成功'
    accountedit=Account.objects.all().order_by("project_id")
    return render_to_response("accountinput_edit.html",locals())
    
def accountinput_del_submit(request):
    try:
        person_show=name = request.session["Uid"]
    except:
        return render_to_response( "login.html",{'nameerror':'非法'})
    bill_sqlid=request.POST["bill_sqlid"]
    pwd=request.POST["pwd"]
    obj1 = Bill.objects.get(id = bill_sqlid)
    fini_person=obj1.transactor
    obj2 = User.objects.get(uid=fini_person)
    if obj2.password != pwd:
        error='密码不正确'
        accountedit=Account.objects.all().order_by("project_id")
        return render_to_response("accountinput_edit.html",locals())
    obj3=Prokindaccount.objects.get( proid = obj1.proid , payname = obj1.paykind )
    obj3.money_cost=obj3.money_cost - obj1.money
    obj3.save()
    
    obj4=Account.objects.get( project_id =obj1.proid )
    obj4.money_cost = obj4.money_cost - obj1.money 
    obj4.save()
    
    obj5 = Billchange_record(transactor = obj1.transactor,billsql_id = obj1.id,time = datetime.datetime.now(),proid = obj1.proid,operation= u'删除',)
    obj5.save()
    
    device_del = Billdevice_record.objects.filter(Bill_sqlid = bill_sqlid)
    device_del.delete()
    obj1.delete()
    error='删除成功'
    accountedit=Account.objects.all().order_by("project_id")
    return render_to_response("accountinput_edit.html",locals())
