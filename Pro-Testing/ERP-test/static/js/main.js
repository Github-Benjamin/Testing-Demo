/**
 * Created by admin on 2017/8/22.
 */

$(document).ready(function () {

    var jedata = function () {
        $(".selecttime").jeDate({
            isinitVal:false,
            //festival:true,
            ishmsVal:false,
            minDate: '2017-06-06 00:00',
            format:"YYYY-MM-DD hh:mm",
            zIndex:3000,
        })
    };

    var i=1;
    jedata();

    $('#addclass').click(function () {
        var tr = '<tr id="tr'+i+'">' +
            '<td><input type="text" name="pname'+i+'" required="required"  size="8"></td>' +
            '<td><input type="text" name="pguige'+i+'"  size="8"></td>' +
            '<td><input type="text" name="pchenbenjia'+i+'" size="8"></td>' +
            '<td><input type="text" name="pxiaoshoujia'+i+'" size="8"></td>' +
            '<td><input type="text" class="selecttime" name="psctime'+i+'"placeholder="选择时间" size="11"></td>' +
            '<td><input type="text" class="selecttime" name="pyxtime'+i+'"placeholder="选择时间" size="11"></td>' +
            '<td><input type="text" class="selecttime" name="pjhtime'+i+'"placeholder="选择时间"  required="required" size="11"></td></tr>';
        $('.addtr').before(tr);
        jedata();
        i++;
    });

    $('#delclass').click(function () {
        i--;
        var tr= $('#tr'+i);
        tr.remove();
    });

    $('.editdata b i').click(function () {
        $('.editdata').fadeOut();
    });
});

function Getid(obj){
    var id=(obj.id);
    $('.editdata').fadeIn();
    $.getJSON("/edit",{id:id},function (data,textStatus,jqXHR) {
        $('#editid').attr("value",data[0].id);
        $('#editpxiaoshoujia').attr("value",data[0].pxiaoshoujia);
        $('#editpguige').attr("value",data[0].pguige);
        $('#editpyxtime').attr("value",data[0].pyxtime);
        $('#editpchenbenjia').attr("value",data[0].pchenbenjia);
        $('#editpname').attr("value",data[0].pname);
        $('#editpjhtime').attr("value",data[0].pjhtime);
        $('#editpsctime').attr("value",data[0].psctime);
    });
};
