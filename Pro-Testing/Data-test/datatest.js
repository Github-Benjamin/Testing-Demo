/**
 * Created by admin on 2017/8/29.
 */


$.ajax({
    type: "GET",
    url: 'http://127.0.0.1:8080/test/1',
    dataType:'json',
    success: function(data){

        // $('.box').append(data.data[0].pjhtime);
        $.each(data, function (n, value) {
            $.each(value, function (n, value) {
                var tddata = '<tr class="jsonadd"><td>' + value.id + '</td><td>' + value.pname + '</td><td>' + value.pguige + '</td><td>' + value.pchenbenjia + '</td><td>' + value.pxiaoshoujia + '</td><td>' + value.psctime + '</td><td>' + value.pyxtime + '</td><td>' + value.pjhtime
                $(".table").append(tddata);
            });
        });
        $(".pagenum").remove();
        $(".box").append('<br class="pagenum"><i class="pagenum"> 当前页数：'+data.page+' </i></br>');
    }
});