$(function(){
    $("#godown").click(function(){
        jQuery("html,body").animate({
            scrollTop: $('#container').offset().top
        },1000);
    });
});