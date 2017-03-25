$(function(){
    var len = 45; // 超過45個字以"..."取代
    $("#block > .text > #brief").each(function(i){
        if($(this).text().length>len){
            var text=$(this).text().substring(0,len-1)+"...";
            $(this).text(text);
        }
    });
});

/*$(function(){
    var len = 9; // 超過9個字以"..."取代
    $("#block > #more_info > p#location").each(function(i){
        if($(this).text().length>len){
            var text=$(this).text().substring(0,len-1)+"...";
            $(this).text(text);
        }
    });
});*/