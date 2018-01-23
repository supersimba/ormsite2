$(document).ready(function() {
	$('#a-sidermenu-collape').bind('click',function(){
		if($('.ul-sider-menu').css('display')=='none')
		{
			$('.ul-sider-menu').show();
			$('.div-sider-menu').show();
			console.log($('.content-body').css('margin-left'));
			if($('.content-body').css('margin-left')=='0px')
			{
				
				$('.content-body').css('margin-left','200px');
			}
			
		}
		else
		{
			$('.ul-sider-menu').hide();
			$('.div-sider-menu').hide();
			console.log($('.content-body').css('margin-left'));
			if($('.content-body').css('margin-left')=='200px')
			{
				$('.content-body').css('margin-left','0px');
			}
		}
	});
	
	$('#a-jk-list').bind('click',function()
	{
		if($('#ul-sub-jk-list').css('display')=='none')
		{
			$('#ul-sub-jk-list').show();
			$('#ul-sub-jk-gl').hide();
			
			$('#fa-jk-list-left').hide();
			$('#fa-jk-list-down').show();
			$('#fa-jk-gl-left').show();
			$('#fa-jk-gl-down').hide();
		}
		else{
			$('#ul-sub-jk-list').hide();
			
			$('#fa-jk-list-left').show();
			$('#fa-jk-list-down').hide();
			$('#fa-jk-gl-left').show();
			$('#fa-jk-gl-down').hide();
		}
	});
	$('#a-jk-gl').bind('click',function()
	{
		if($('#ul-sub-jk-gl').css('display')=='none')
		{
			$('#ul-sub-jk-gl').show();
			$('#ul-sub-jk-list').hide();
			
			$('#fa-jk-gl-left').hide();
			$('#fa-jk-gl-down').show();
			$('#fa-jk-list-left').show();
			$('#fa-jk-list-down').hide();
		}
		else{
			$('#ul-sub-jk-gl').hide();
			$('#fa-jk-gl-left').show();
			$('#fa-jk-gl-down').hide();
			
			$('#fa-jk-list-left').show();
			$('#fa-jk-list-down').hide();
		}
	});
});