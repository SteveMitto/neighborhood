$(document).ready(function(){
  var windowSize= $(window).width()
  if(windowSize  < 700){
    $(".chat-main .chat-main-child").css({"width":"100%"})
    $(".chat-main").css({"padding":"0"})
  }else{
    $(".chat-main").css({"padding":"0 15px"})
    $(".chat-main .chat-main-child").css({"width":"60%"})
  }
  $(window).on('resize',function(){
    windowSize = $(window).width()
    if(windowSize  < 700){
      $(".chat-main .chat-main-child").css({"width":"100%"})
      $(".chat-main").css({"padding":"0"})
    }else{
      $(".chat-main").css({"padding":"0 15px"})
      $(".chat-main .chat-main-child").css({"width":"60%"})
    }
  })
})
