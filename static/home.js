$(function() {
    // nav样式
    $(".nav .index li").eq(0).children().css({
        top: "-10px"
        });
    $(".nav .index li").eq(0).nextAll().children().css({
        top: "-90px"
        });
    $(".nav .index li").eq(3).nextAll().children().css({
        top: "-330px"
        });
    $(".nav .tri").css({
        top: "50%",
        marginTop: "-5px"
    });
    // 
    // PageNum 样式
    $("#PageNum").children().css({
        float: "left"
    })
    
})