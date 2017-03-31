$(function(){
　　$(window).bind('scroll resize', function(){
　　var $this = $(this);
　　var this_Top=$this.scrollTop();
	var limit=$(window).height();

　　if(this_Top < limit){
		$('#head').stop().animate({color: "rgb(240, 255, 255)"});
		$('#head > .arrow-up').stop().animate({left: "11.5%"});
		$('#head > .arrow-up2').stop().fadeOut(1).animate({left: "11.5%"});
	}
	if((limit*3.5)<this_Top && this_Top<=(limit*4.5)){
		$('#head').stop().animate({color: "rgb(240, 255, 255)"});
		$('#head > .arrow-up').stop().animate({left: "60%"});
		$('#head > .arrow-up2').stop().fadeOut(1).animate({left: "60%"});
	}
　　if((limit)<this_Top && this_Top<=(limit*3.5)){
		$('#head').stop().animate({color: "rgb(15,24,43)"});
		$('#head > .arrow-up').stop().animate({left: "35.75%"});
		$('#head > .arrow-up2').stop().fadeIn(1).animate({left: "35.75%"});
	}
　　if((limit*4.5)<this_Top && this_Top<=(limit*5.5)){
		$('#head').stop().animate({color: "rgb(15,24,43)"});
		$('#head > .arrow-up').stop().animate({left: "84.25%"});
		$('#head > .arrow-up2').stop().fadeIn(1).animate({left: "84.25%"});
	}
　　}).scroll();
});

$(function(){
	var limit=$(".p1").height();
    $(".option1").click(function(){
        jQuery("html,body").animate({
            scrollTop: $('.p1').offset().top
        },500);
    });
	$(".option2").click(function(){
        jQuery("html,body").animate({
            scrollTop: $('.p2').offset().top
        },500);
    });
	$(".option3").click(function(){
        jQuery("html,body").animate({
            scrollTop: $('.p5').offset().top
        },500);
    });
	$(".option4").click(function(){
        jQuery("html,body").animate({
            scrollTop: $('.p6').offset().top
        },500);
    });
});