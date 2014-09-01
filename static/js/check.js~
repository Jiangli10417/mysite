$(document).ready(function(){
    $("#submit").bind('click',function(){
        var time = $("#time").val();
        var project = $("#project").val();
        var name = $("#name").val();
        var money = $("#money").val();
        var num = $("#num").val();
        var person = $("#person").val();
        var pnum = $("#pnum").val();    
        if(!isNaN(project))
        {
            $("#promsg").html("数据库错误请联系工作人员");
            return false;
        }

        if(!time)
        {
            $("#timemsg").html("时间不能为空！");
            return false;
        }
        if(!name)
        {
            $("#namemsg").html("请填写名称");
            return false;
        }
        if(!money)
        {
            $("#moneymsg").html("请填写金额");
            return false;
        }
        var re = new RegExp(".","g");
        var arr = money.match(re);
        var len = arr.length;
        var loc = money.lastIndexOf(".")
        if (len != 1 || loc !=3  )
        {
            $("#moneymsg").html("金额格式错误");
            return false;
        }
        
        if (!(/^[1-9]([0-9\.]+\d)?$/.test(money)))
        {
            $("#moneymsg").html("必须为数字");
            return false;
        }
        
        if(!isNaN(num))
        {
            $("#nummsg").html("必须为数字")
            return false;
        }
        if(!person)
        {
            $("#person").html("经办人不能为空");
            return false;
        }
        if(!pnum || !isNaN(num))
        {
            $("#pnum").html("票据号错误");
            return false;
        }
        return true;
        
    });
    
    $("#project").bind("change",function(){
        var project = $(this).val();
        if(project ="001"){
            alert(project);
        }
        $("#projectid").append("<option value='123'>123</option>");
    })
   
});
