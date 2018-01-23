// orminfo表格，获得同步信息,from db








function getdbinfo(rid,trobj,trobj_collape)
{
	$.ajax({
		type:"POST",
        async:true,
        dataType:"json",
        data:{rid:rid},
        url: "/display_target_info/",
    	beforeSend:function () {
        	
        },
        success:function(callback,status,xhr){
        	//console.log(callback['record_flag']);
        	if(callback['record_flag']==-1)
        	{

        		for(var m=6;m<=9;m++){
        			trobj.children().eq(m).css('background','#FFFFCC');
        		}
        	}
        	else
        	{
        		for(var m=6;m<=9;m++){
        			trobj.children().eq(m).css('background','white');
        		}
        		//trobj.children().eq(2).css('background','#FFFFCC');
        		if(callback["ssh_status"]==1 && callback["path_status"]==1 && callback["script_status"]==1)
                {
           //      	for(var m=1;m<=2;m++)
           //          {
        			// 	trobj.children().eq(m).css('background','white');
        			// }
                    trobj.children().eq(6).css('background','white');
                    trobj.children().eq(7).html(settgtstatus(callback["sync_status"]));
                    trobj.children().eq(8).html(settgtactive(callback["active"]));
                    trobj.children().eq(9).text(callback["add_time"].substring(4));
                    trobj_collape.find('.tr-collape-tgt').children().eq(1).children('#span-collect-num').text(callback['collect_cnt']);
                    trobj_collape.find('.tr-collape-tgt').children().eq(2).children('#span-loader-s-profile').text(callback['loader_s_p_cnt']);
                    trobj_collape.find('.tr-collape-tgt').children().eq(2).children('#span-loader-s').text(callback['loader_s_cnt']);

                    trobj_collape.find('.tr-collape-tgt').children().eq(3).children('#span-loader-r-profile').text(callback['loader_r_p_cnt']);
                    trobj_collape.find('.tr-collape-tgt').children().eq(3).children('#span-loader-r').text(callback['loader_r_cnt']);


                    trobj_collape.find('.tr-collape-tgt').children().eq(4).children('#span-loader-rate').text(callback['loader_rate']);
                    trobj_collape.find('.tr-collape-tgt').children().eq(5).children('#span-loader-err').text(callback['loader_err']);

                    trobj_collape.find('.tr-collape-ldrtime').children().eq(1).children('#span-loader-time').text(callback['loader_time']);
                }
                else
                {
           //          for(var m=1;m<=2;m++)
           //          {
        			// 	trobj.children().eq(m).css('background','rgb(248,108,107)');
        			// }
                    trobj.children().eq(6).css('background','rgb(248,108,107)');
                }


        	}
        },
        error:function (XMLResponse) {
                    console.log("数据抓取失败");
        }
    })
}




function displayrepinfo(){
	for(var i=0;i<$('#table-info-tbody').children().length;i++)
    {
        if(i%2==0)
        {
            var trobj = $('#table-info-tbody').children().eq(i);
            var trobj_collape = $('#table-info-tbody').children().eq(i+1);
            var rid = trobj.children().eq(0).children('.span-rid').eq(0).text();
            getdbinfo(rid,trobj,trobj_collape);
        }
    }
}





$(document).ready(function($) {
	
});