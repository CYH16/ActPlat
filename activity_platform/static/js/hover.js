$(function(){
	$("#content > a > #block").hover(
	function(){
		$(this).css("background","rgba(240, 255, 255, 1)");
		$(this).css("color","rgb(15,24,43)");
		$(this).children(".text").children("#time").css("color","rgb(15,24,43)");
		$(this).children(".text").children("#brief").css("color","rgb(15,24,43)");
	},
	function(){
		$(this).css("background","rgba(240, 255, 255, 0)");
		$(this).css("color","rgba(240, 255, 255, 1)");
		$(this).children(".text").children("#time").css("color","rgba(240, 255, 255, 1)");
		$(this).children(".text").children("#brief").css("color","rgba(240, 255, 255, .4)");
	});
});

$(function(){
	$(".p1 > .title > form > input").hover(
	function(){
		$(this).css("background","rgba(240, 255, 255, 1)");
		$(this).css("color","rgb(15,24,43)");
	},
	function(){
		$(this).css("background","rgba(240, 255, 255, 0)");
		$(this).css("color","rgba(240, 255, 255, 1)");
	});
});