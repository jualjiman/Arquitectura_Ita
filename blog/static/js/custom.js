//opacity navbar menu
$(document).on("scroll",function(){
    console.log("meeeh");
    if($(document).scrollTop()>200){
        $(".square-button.sticky.fixed.effect").fadeIn();

    } else{
        $(".square-button.sticky.fixed.effect").fadeOut();
    }
});
