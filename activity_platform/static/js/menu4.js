$(function(){
	$(".option").hover(
	function(){
		$(this).children(".selection").stop().slideDown(300);
	}, 
	function(){
		$(this).children(".selection").stop().slideUp(300);
	});
});

var selected = [0,[0,1,1,1,1,1],[0,1,1,1,1,1],[0,1,1,1,1,1],[0,1,1,1,1,1],[0,1,1,1,1,1]];
var keyword = [0,[0,"a","b","c","d","e"],[0,"學校活動","學生會","系學會","社團活動","其他"],[0,"室內．學術","室內．休閒","戶外．運動","戶外．休閒","其他"],[0,"免費且備餐","免費","每人0-100元","每人101-500元","每人500元以上"],[0,"不限","校內學生","系內限定","社團限定",""]];

$(function(){

	$(".selection li").stop().click(function(){
		id = $(this).attr('id');
		category = parseInt(id.substring(0));
		parameter = parseInt(id.substring(2));
		if(selected[category][parameter]==0){
			$(this).css("background","rgba(240, 255, 255, 1)");
			$(this).children("#slider").css("background","rgb(15,24,43)");
			$(this).children("#slider").children("#switch").css("background","rgba(240, 255, 255, 1)");
			$(this).children("#slider").children("#switch").removeClass("to_left").addClass("to_right");
			selected[category][parameter]=1;
			show_selected();
		}
		else if(selected[category][parameter]==1){
			$(this).css("background","rgba(126, 138, 150, 1)");
			$(this).children("#slider").css("background","rgba(83, 93, 105, 1)");
			$(this).children("#slider").children("#switch").css("background","rgba(126, 138, 150, 1)");
			$(this).children("#slider").children("#switch").removeClass("to_right").addClass("to_left");
			selected[category][parameter]=0;
			show_selected();
		}
	});

});
function show_selected(){
	var selectedClass = "";
	$("#content").stop().fadeTo(1, 0).delay(200);
	$("#content > a > div#block").addClass("show").removeClass("hide");
	for(i=1;i<=5;i++){
		for(j=1;j<=5;j++){
			if(selected[i][j]==0){
				selectedClass = keyword[i][j];
				$("#content > a > div#block."+selectedClass).addClass("hide").removeClass("show");
			}
		}
	}
	$("#content > a > div#block.hide").fadeOut(200);
	$("#content > a > div#block.show").fadeIn(200);
	$("#content").fadeTo(500, 1);
}