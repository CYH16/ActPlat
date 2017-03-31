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
	if((limit)<this_Top && this_Top<=(limit*2)){
		$('.p2  > .title2_text').animate({left: "40%"});
	}
	
	if((limit)<this_Top && this_Top<=(limit*2)){
		$('.p3  > .title3').delay(500).fadeIn(1000);
	}
	
	if((limit*1.5)<this_Top && this_Top<=(limit*2.3)){
		$('.p3  > .title3_2').delay(500).fadeIn(1000);
	}
	
	if((limit*2.3)<this_Top && this_Top<=(limit*3.5)){
		$('.p4  > .title2_text').animate({left: "40%"});
	}
	
　　if((limit*3.5)<this_Top && this_Top<=(limit*4.5)){
		$('.p5  > .title5_text').animate({left: "40%"});
	}

　　if((limit*4.5)<this_Top && this_Top<=(limit*6)){
		$('.p6 > .title6_text').animate({left: "40%"});
	}
	
　　}).scroll();
});