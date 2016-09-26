$(function(){
   $(".square-button.sticky.fixed").hide();
});

$(document).on("scroll",function(){
    if($(document).scrollTop()>200){
        $(".square-button.sticky.fixed").fadeIn();

    } else{
        $(".square-button.sticky.fixed").fadeOut();
    }
});
