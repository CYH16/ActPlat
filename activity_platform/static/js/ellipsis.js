$(function(){
    var len = 64; // 超過64個字以"..."取代
    $("#block > #brief").each(function(i){
        if($(this).text().length>len){
            var text=$(this).text().substring(0,len-1)+"...";
            $(this).text(text);
        }
    });
});