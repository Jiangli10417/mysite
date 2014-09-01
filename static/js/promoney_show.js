$(document).ready(function(){
    $("#proid").change(function(){
        var procheck;
                
        procheck = $(this).children('option:selected').val();  
        if( procheck == "863" )
        {
            var txt1="                    <tr>
                                                    <td>设备费</td>
                                                    <td>{{moneykind.moneyac}}</td>
                                                    <td><input type="text" class="form-control" id={{moneykind.name}} name={{moneykind.name}} ></td>
                                                    <td>
                                                        <select class="form-control" id="moneysourse" name="moneysourse">
                                                           <option>国家下拨</option>
                                                           <option>省级下拨</option>
                                                           <option>院校下拨</option>
                                                           <option>资金自筹</option>
                                                        </select>
                                                     </td>
                                                </tr>";
        }
      
      });
})
