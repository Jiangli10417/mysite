#encoding=utf-8
from django.conf.urls import patterns, include, url

import engine
from engine import login,manager,financial,responsible,systemuser
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^logincheck/$', engine.login.logincheck),
    url(r'^logout/$', engine.login.logout),
    url(r'^$', engine.login.login),
    
    url(r'^kindconedit/$',engine.manager.kindconedit),
    url(r'^kindconedit_add/$',engine.manager.kindconedit_add),
    url(r'^kindconedit_add_edit/$',engine.manager.kindconedit_add_edit),
    url(r'^kindconedit_showcontent/$',engine.manager.kindconedit_showcontent),
    url(r'^kindconedit_del/$',engine.manager.kindconedit_del),
    
    
    url(r'^tempedit/$',engine.manager.tempedit),
    url(r'^tempedit_add/$',engine.manager.tempedit_add),
    url(r'^tempedit_showcontent/$',engine.manager.tempedit_showcontent),
    url(r'^tempedit_add_edit/$',engine.manager.tempedit_add_edit),
    url(r'^tempedit_del/$',engine.manager.tempedit_del),
    
    url(r'^accountinput_edit/$',engine.manager.accountinput_edit),
    url(r'^accountinput_edit_show/$',engine.manager.accountinput_edit_show),
    url(r'^accountinput_edit_check/$',engine.manager.accountinput_edit_check),
    url(r'^accountedit_kindcontent_show/$',engine.manager.accountedit_kindcontent_show),
    url(r'^accountinput_edit_submit/$',engine.manager.accountinput_edit_submit),
    url(r'^accountinput_del_submit/$',engine.manager.accountinput_del_submit),
    
    
    url(r'^account_create_edit/$',engine.financial.account_create_edit),
    url(r'^accountcreate/$',engine.financial.accountcreate),
    url(r'^accountedit/$',engine.financial.accountedit),
    url(r'^accountcreate_create/$',engine.financial.accountcreate_create),
    
    url(r'^accountinput_create/$',engine.financial.accountinput_create),
    url(r'^accountinput_create_select/$',engine.financial.accountinput_create_select),
    url(r'^accountcreate_kindcontent_show/$',engine.financial.accountcreate_kindcontent_show),
    url(r'^accountinput_create_input/$',engine.financial.accountinput_create_input),

    url(r'^billquery/$',engine.financial.billquery),
    url(r'^billquery_show/$',engine.financial.billquery_show),
    url(r'^billprocontent_show/$',engine.financial.billprocontent_show),
    
    url(r'^accountadd/$',engine.financial.accountadd),
    url(r'^accountadd_add/$',engine.financial.accountadd_add),
    url(r'^accountadd_edit/$',engine.financial.accountadd_edit),
    url(r'^accountadd_add_input/$',engine.financial.accountadd_add_input),
    url(r'^accountadd_edit_input/$',engine.financial.accountadd_edit_input),
    
    url(r'^responsible_account/$',engine.responsible.responsible_account),
    url(r'^responsible_account_show/$',engine.responsible.responsible_account_show),
    url(r'^responsible_pro/$',engine.responsible.responsible_pro),
    url(r'^responsible_pro_show/$',engine.responsible.responsible_pro_show),
    url(r'^responsible_pro_show_kind/$',engine.responsible.responsible_pro_show_kind),
    
    url(r'^responsible_all/$',engine.responsible.responsible_all),
    url(r'^responsible_all_kindshow/$',engine.responsible.responsible_all_kindshow),
    
    url(r'^responsible_account_finish/$',engine.responsible.responsible_account_finish),
    url(r'^responsible_account_finish_show/$',engine.responsible.responsible_account_finish_show),

    url(r'^responsible_account_year/$',engine.responsible.responsible_account_year),
    url(r'^responsible_account_year_show/$',engine.responsible.responsible_account_year_show),
    
    url(r'^responsible_billchange_record/$',engine.responsible.responsible_billchange_record),
    url(r'^responsible_billchange_record_show/$',engine.responsible.responsible_billchange_record_show),
    
    url(r'^systemuser_userinput/$',engine.systemuser.systemuser_userinput),
    url(r'^systemuser_userinput_input/$',engine.systemuser.systemuser_userinput_input),
    
    url(r'^systemuser_useredit/$',engine.systemuser.systemuser_useredit),
    url(r'^systemuser_useredit_show/$',engine.systemuser.systemuser_useredit_show),
    url(r'^systemuser_useredit_edit/$',engine.systemuser.systemuser_useredit_edit),
    
    url(r'^systemuser_userchange/$',engine.systemuser.systemuser_userchange),
    url(r'^systemuser_userchange_del/$',engine.systemuser.systemuser_userchange_del),
    url(r'^systemuser_userchange_del_sub/$',engine.systemuser.systemuser_userchange_del_sub),
    url(r'^systemuser_userchange_ret/$',engine.systemuser.systemuser_userchange_ret),
    url(r'^systemuser_userchange_ret_sub/$',engine.systemuser.systemuser_userchange_ret_sub),
    
    url(r'^systemuser_pwdreset/$',engine.systemuser.systemuser_pwdreset),
    url(r'^systemuser_pwdreset_sub/$',engine.systemuser.systemuser_pwdreset_sub),
    #url(r'^tempedit',engine.manager.tempedit)
    #url(r'account/create_prosearch',engine.account.create_search),
    #url(r'account/create_proshow',engine.account.create_proshow),    #帐号创建显示信息
    #url(r'account/create',engine.account.create),
    #url(r'account/success',engine.account.create_success),
    
    #url(r'account/input_search',engine.account_input.input_search),
    #url(r'account/cost_input',engine.account_input.cost_input),
    #url(r'account/input_continue',engine.account_input.input_continue),
    #url(r'account/input_finish',engine.account_input.input_finish),
   
    #url(r'account/money_add',engine.account_input.money_add),
    #url(r'account/add_search',engine.account_input.add_search),
    #url(r'account/result_check',engine.account_input.result_check),
    
    #url(r'search/project',engine.search.showpro),
    
    #url(r'acc_spend/search',engine.acc_spend.search),
    #url(r'acc_spend/spend_show',engine.acc_spend.spendshow),
#    url(r'account/account_input',engine.account.account_input),
#    url(r'account/result_check',engine.account.result_check),输入结果检
#    url(r'account/account_addsearch',engine.account.account_addsearch),经费追加查询
#    url(r'account/account_add',engine.account.account_add),经费追加
#    url(r'account/result_check863',engine.account.account_add),
   #  url(r'^$',engine.index.welcom)
   
  
#    url(r'account/create_one',engine.account.create_one),    

)
