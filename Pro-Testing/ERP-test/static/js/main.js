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


    // Ajax 分页处理逻辑
    var page = 0;
    var Refresh = function () {
        var url = '/jsonpage/'+page;
        $.ajax({
            type: "GET",
            url: url,
            dataType:'json',
            success: function(data){
                $(".jsonadd").remove();
                $.each(data, function (n, value) {
                    var tddata= '<tr class="jsonadd"><td>'+value.id+'</td><td>'+value.pname+'</td><td>'+value.pguige+'</td><td>'+value.pchenbenjia+'</td><td>'+value.pxiaoshoujia+'</td><td>'+value.psctime+'</td><td>'+value.pyxtime+'</td><td>'+value.pjhtime+'</td><td>&nbsp;&nbsp;<a href="javascript:;" onclick="Getid(this);" id="'+value.id+'" style="text-decoration:none;">编辑</a>&nbsp;&nbsp;<a href=javascript:if(confirm("确实要删除该内容吗?"))location="/del?id='+value.id+'" style="color: #ff0000;text-decoration:none;">删除</a>&nbsp;&nbsp;</td></tr>'
                    $(".jsondatalist").append(tddata);
                });
                $(".pagenum").remove();
                $(".pagedn").before('<i class="pagenum"> 当前页数：'+(page+1)+' </i>');
            }
        });
    }

    Refresh();
    // 上一页

    $('.pageup').click(function( ) {
        if(page<=0){return alert('目前已是首页！')}
        if(page>0){var url = '/jsonpage/'+(page-1);page=page-1;}
        $.ajax({
            type: "GET",
            url: url,
            dataType:'json',
            success: function(data){
                $(".jsonadd").remove();
                $.each(data, function (n, value) {
                    var tddata= '<tr class="jsonadd"><td>'+value.id+'</td><td>'+value.pname+'</td><td>'+value.pguige+'</td><td>'+value.pchenbenjia+'</td><td>'+value.pxiaoshoujia+'</td><td>'+value.psctime+'</td><td>'+value.pyxtime+'</td><td>'+value.pjhtime+'</td><td>&nbsp;&nbsp;<a href="javascript:;" onclick="Getid(this);" id="'+value.id+'" style="text-decoration:none;">编辑</a>&nbsp;&nbsp;<a href=javascript:if(confirm("确实要删除该内容吗?"))location="/del?id='+value.id+'" style="color: #ff0000;text-decoration:none;">删除</a>&nbsp;&nbsp;</td></tr>'
                    $(".jsondatalist").append(tddata);
                });
                $(".pagenum").remove();
                $(".pagedn").before('<i class="pagenum"> 当前页数：'+(page+1)+' </i>');
            }
        });
    })


    // 下一页
    $('.pagedn').click(function( ) {
        if(page>=0){var url = '/jsonpage/'+(page+1);page=page+1;}
        $.ajax({
            type: "GET",
            url: url,
            dataType:'json',
            success: function(data){
                if(data.length){
                    $(".jsonadd").remove();
                    $.each(data, function (n, value) {
                        var tddata= '<tr class="jsonadd"><td>'+value.id+'</td><td>'+value.pname+'</td><td>'+value.pguige+'</td><td>'+value.pchenbenjia+'</td><td>'+value.pxiaoshoujia+'</td><td>'+value.psctime+'</td><td>'+value.pyxtime+'</td><td>'+value.pjhtime+'</td><td>&nbsp;&nbsp;<a href="javascript:;" onclick="Getid(this);" id="'+value.id+'" style="text-decoration:none;">编辑</a>&nbsp;&nbsp;<a href=javascript:if(confirm("确实要删除该内容吗?"))location="/del?id='+value.id+'" style="color: #ff0000;text-decoration:none;">删除</a>&nbsp;&nbsp;</td></tr>'
                        $(".jsondatalist").append(tddata);
                    });
                    $(".pagenum").remove();
                    $(".pagedn").before('<i class="pagenum"> 当前页数：'+(page+1)+' </i>');
                }else {
                    page=page-1;
                    return alert('目前已是尾页！')
                }
            }
        });
    })

    // 修改数据实现异步提交不用重新刷新页面
    $(".submit").click(function () {
        var data = {
            'id':$('#editid').val(),
            'pname':$('#editpname').val(),
            'pguige':$('#editpguige').val(),
            'pchenbenjia':$('#editpchenbenjia').val(),
            'pxiaoshoujia':$('#editpxiaoshoujia').val(),
            'psctime':$('#editpsctime').val(),
            'pyxtime':$('#editpyxtime').val(),
            'pjhtime':$('#editpjhtime').val(),
        }
        $.ajax({
            type: "POST",
            url: "/edit",
            dataType:'json',
            data:data,
            success: function(data){
                if(data){
                    if(data.code == 200){
                        Refresh();
                        $('.editdata').fadeOut();
                        return alert('修改成功');
                    }
                    else {
                        $('.editdata').fadeOut();
                        alert('修改失败');
                    }
                }
            }
        });
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
