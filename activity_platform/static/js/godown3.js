$(function(){
    $(".p2 > img").click(function(){
        jQuery("html,body").animate({
            scrollTop: $('.p3').offset().top
        },1000);
    });
	
    $(".p3 > img.godown").click(function(){
        jQuery("html,body").animate({
            scrollTop: $('.p3 > .anchor').offset().top
        },1000);
    });
});