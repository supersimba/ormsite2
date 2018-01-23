// orminfo表格，获得源端信息



//设置同步状态
function setsrcstatus(val) {
    // console.log(val);
    switch (val)
    {
        case -1:
            //return "<i class=\"fa fa-remove\" style='color: red;'></i>";
        	return "<span style='font-size: 11px;background: rgb(255,193,7);border: 0px;color: white;padding: 3px;'>告警</span>"
        case 0:
            return "<span style='font-size: 11px;background: rgb(164,183,193);border: 0px;color: white;padding: 3px;'>停止</span>"
        case 1:
        	return "<span style='font-size: 11px;background: rgb(77,189,116);border: 0px;color: white;padding: 3px;'>运行</span>"
            // return "<i class=\"fa fa-arrow-up\" style='color: lawngreen;'></i>";
            //return "<img src='/static/img/stop.png'></img>";
    }
}


// 设置同步动作
function setsrcactive(val) {
    console.log(val);
    switch (val)
    {
        case 0:
            return "<span style='font-size: 11px;background: rgb(164,183,193);border: 0px;color: white;padding: 3px;'>停止</span>"
        case 1:
            return "<span style='font-size: 11px;background: rgb(77,189,116);border: 0px;color: white;padding: 3px;'>待机</span>"
        case 2:
            return "<span style='font-size: 11px;background: rgb(77,189,116);border: 0px;color: white;padding: 3px;'>分析</span>"
    }
}


function getsrcdbinfo(rid,trobj,trobj_collape)
{
	$.ajax({
		type:"POST",
        async:true,
        dataType:"json",
        data:{rid:rid},
        url: "/display_source_info/",
    	beforeSend:function () {
        	
        },
        success:function(callback,status,xhr){
        	//console.log(callback['record_flag']);
        	if(callback['record_flag']==-1)
        	{

        		for(var m=1;m<=5;m++){
        			trobj.children().eq(m).css('background','#FFFFCC');
        		}
        	}
        	else
        	{
        		for(var m=1;m<=5;m++){
        			trobj.children().eq(m).css('background','white');
        		}
        		//trobj.children().eq(2).css('background','#FFFFCC');
        		if(callback["ssh_status"]==1 && callback["path_status"]==1 && callback["script_status"]==1)
                {
                	for(var m=1;m<=2;m++)
                    {
        				trobj.children().eq(m).css('background','white');
        			}
                    trobj.children().eq(3).html(setsrcstatus(callback["sync_status"]));
                    trobj.children().eq(4).html(setsrcactive(callback["active"]));
                    trobj.children().eq(5).text(callback["add_time"].substring(4));
                    trobj_collape.find('.tr-collape-src').children().eq(1).children('#span-dbps-num').text(callback['dbps_cnt']);
                    trobj_collape.find('.tr-collape-src').children().eq(2).children('#span-vag-num').text(callback['capture_cnt']);
                    trobj_collape.find('.tr-collape-src').children().eq(3).children('#span-sender-num').text(callback['sender_cnt']);
                    trobj_collape.find('.tr-collape-src').children().eq(4).children('#span-vag-err').text(callback['capture_err']);
                    trobj_collape.find('.tr-collape-src').children().eq(5).children('#span-sender-err').text(callback['sender_err']);
                    // trobj_plus.children().eq(0).children().eq(2).children('#span-loader-time').text(callback['loader_time']);
                }
                else
                {
                    // for(var m=1;m<=2;m++)
                    // {
        			trobj.children().eq(2).css('background','rgb(248,108,107)');
        			// }
                }


        	}
        },
        error:function (XMLResponse) {
                    console.log("数据抓取失败");
        }
    })
}


function displaysrcinfo() 
{
    for(var i=0;i<$('#table-info-tbody').children().length;i++)
    {
        if(i%2==0)
        {
            var trobj = $('#table-info-tbody').children().eq(i);
            var trobj_collape = $('#table-info-tbody').children().eq(i+1);
            var rid = trobj.children().eq(0).children('.span-rid').eq(0).text();
            getsrcdbinfo(rid,trobj,trobj_collape);
        }
    }
}

 function freshsrcinfo(fnc,wait)
 {
    var interv = function()
    {
        fnc.call(null);
        setTimeout(interv,wait);
    }
    setTimeout(interv,wait);
 }

$(document).ready(function() {
	// freshsrcinfo(displaysrcinfo,60000);
    setInterval(displaysrcinfo,30000);
});