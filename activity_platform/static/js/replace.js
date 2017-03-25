$(function(){
	$("#block > .text > #time").each(function(i){
		var text = $(this).text().replace(/Mon/g,"一");
		text = text.replace(/Tue/g,"二");
		text = text.replace(/Wed/g,"三");
		text = text.replace(/Thu/g,"四");
		text = text.replace(/Fri/g,"五");
		text = text.replace(/Sat/g,"六");
		text = text.replace(/Sun/g,"日");
		$(this).text(text);
	});
	$(".p3 > .wrapper > .info > .text_date > .start_date").each(function(i){
		var text = $(this).text().replace(/Mon/g,"一");
		text = text.replace(/Tue/g,"二");
		text = text.replace(/Wed/g,"三");
		text = text.replace(/Thu/g,"四");
		text = text.replace(/Fri/g,"五");
		text = text.replace(/Sat/g,"六");
		text = text.replace(/Sun/g,"日");
		$(this).text(text);
	});
	$(".p3 > .wrapper > .info > .text_date > .end_date").each(function(i){
		var text = $(this).text().replace(/Mon/g,"一");
		text = text.replace(/Tue/g,"二");
		text = text.replace(/Wed/g,"三");
		text = text.replace(/Thu/g,"四");
		text = text.replace(/Fri/g,"五");
		text = text.replace(/Sat/g,"六");
		text = text.replace(/Sun/g,"日");
		$(this).text(text);
	});
});

$(function(){
	$("#block > #more_info > #deadline").each(function(i){
		if($(this).html()==""){
			$(this).html("<span style='font-size:15px;height:40px;line-height:40px;'>不須報名</span>");
		}
	});
	$(".p3 > .wrapper > .info > .text_deadline").each(function(i){
		if($(this).html()==""){
			$(this).html("不須報名");
		}
	});
});

$(function(){
	$(".p1 > .title > .title_subtext").each(function(i){
		if($(this).html()=="blank"){
			$(this).html("");
		}
	});
});