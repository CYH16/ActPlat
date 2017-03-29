$(function(){
　　$(window).bind('scroll resize', function(){
　　var $this = $(this);
　　var this_Top=$this.scrollTop();
	var limit=$(window).height();

　　/*if(this_Top < limit){
		$('#head').stop().animate({color: "rgb(240, 255, 255)"});
		$('#head > .arrow-up').stop().animate({left: "11.5%"});
		$('#head > .arrow-up2').stop().fadeOut(1).animate({left: "11.5%"});
	}*/
	if((limit*2)<this_Top && this_Top<=(limit*3)){
		$('.p3 > .wrapper').stop().fadeIn();
	}
　　if((limit)<this_Top && this_Top<=(limit*2)){
		$('.p2  > .brief_text').animate({left: "40%"});
	}
　　if((limit*3)<this_Top && this_Top<=(limit*4)){
		$('.p4 > a > .more').stop().fadeIn();
	}
　　}).scroll();
});