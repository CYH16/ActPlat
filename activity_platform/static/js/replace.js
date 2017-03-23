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
});