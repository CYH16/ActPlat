$(function(){
	$(".helptext").each(function(i){
		$(this).html("");
	});
});

$(function(){
	$("label").each(function(i){
		if($(this).html()=="Username:"){
			$(this).html("帳號：");
		}
		if($(this).html()=="Password:"){
			$(this).html("密碼：");
		}
		if($(this).html()=="Password confirmation:"){
			$(this).html("密碼確認：");
		}
	});
});