$(function(){
　　$(window).bind('scroll resize', function(){
　　var $this = $(this);
　　var this_Top=$this.scrollTop();
	var limit=$(window).height()-200;

　　//當高度小於100時，關閉區塊 
　　if(this_Top < limit){
		$('#head').stop().animate({top:"-65px"});
	}
　　if(this_Top > limit){
		$('#head').stop().animate({top:"0px"});
	}
　　}).scroll();
});

$(function(){
	$(".option").hover(
	function(){
		$(this).children(".selection").stop().slideDown(300);
	}, 
	function(){
		$(this).children(".selection").stop().slideUp(300);
	});
});

$(function(){
	var selected = [0,[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]];
	$(".selection li").click(function(){
		id = $(this).attr('id');
		category = parseInt(id.substring(0));
		parameter = parseInt(id.substring(2));
		if(selected[category][parameter]==0){
			$(this).css("background","rgba(0, 225, 228, 1)");
			selected[category][parameter]=1;
		}
		else if(selected[category][parameter]==1){
			$(this).css("background","rgba(240, 255, 255, 1)");
			selected[category][parameter]=0;
		}
	});
});		