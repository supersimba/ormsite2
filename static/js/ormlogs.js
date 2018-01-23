/**
 * Created by root on 17-6-7.
 */

function chkProcess(ip,path,u,p)
{
    $.ajax({
        type:"POST",
        async:true,
        dataType:"text",
        data:{'ip':ip,'path':path,'u':u,'p':p},
        url: "/check_process/",
        success:function (callback) {
            // alert(callback);
            // document.write(callback);
            $('#div-display-log').html(callback)
        },
        error:function (callback) {
            $('#div-display-log').html('进程查看出错')
        }
    });
}


function getSyncLogs(ip,path,u,p,logname) {
    $.ajax({
        type:"POST",
        async:true,
        dataType:"text",
        data:{'ip':ip,'path':path,'u':u,'p':p,'logname':logname},
        url: "/display_log/",
        success:function (callback) {
            $('#div-display-log').html(callback);
            document.getElementById('div-display-log').scrollTop=document.getElementById('div-display-log').scrollHeight;
        },
        error:function (callback) {
            $('#div-display-log').html('日志查看出错')
        }
    });
}

$(document).ready(function () {
    // //查看进程,执行 $DBPS_HOME/scripts/check
    $('.btn-check-pro').bind('click',function(event) {
        ip=$('#span-ip').text();
        path=$('#span-path').text();
        u=$('#span-sshuser').text();
        p=$('#span-sshpwd').text();
        chkProcess(ip,path,u,p);
    });

    // #查看vagentd日志
    $('#btn-vag-log').bind('click',function () {
        ip=$('#span-ip').text();
        path=$('#span-path').text();
        u=$('#span-sshuser').text();
        p=$('#span-sshpwd').text();
        getSyncLogs(ip,path,u,p,'log.vagentd');
    });

    // 查看sender
    $('#btn-sender-log').bind('click',function () {
        ip=$('#span-ip').text();
        path=$('#span-path').text();
        u=$('#span-sshuser').text();
        p=$('#span-sshpwd').text();
        getSyncLogs(ip,path,u,p,'log.sender');
    });


    // 查看log.s.....
    var links_logs=$('.ul-dropdown-menu-s').find('a');

    for(var m=0;m<links_logs.length;m++)
    {
        links_logs.eq(m).bind('click',function (e) {
            var logname="log."+$(this).text();
            ip=$('#span-ip').text();
            path=$('#span-path').text();
            u=$('#span-sshuser').text();
            p=$('#span-sshpwd').text();
            getSyncLogs(ip,path,u,p,logname);
        });
    }

    // 查看log.r...
    var links_logr=$('.ul-dropdown-menu-r').find('a');

    for(var m=0;m<links_logr.length;m++)
    {
        links_logr.eq(m).bind('click',function (e) {
            var logname="log."+$(this).text();
            ip=$('#span-ip').text();
            path=$('#span-path').text();
            u=$('#span-sshuser').text();
            p=$('#span-sshpwd').text();
            getSyncLogs(ip,path,u,p,logname);
        });
    }
});
