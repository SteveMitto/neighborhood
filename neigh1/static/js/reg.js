$(document).ready(function(){
  console.log('ready');
  var screen_width = $(window).width()
  $(".shut").hide()

  if(screen_width<770){
    $(".col-md-2").hide()
    $(".col-md-3").hide()
    $(".menu").slideDown(500)
  }else{
    $(".col-md-2").show()
    $(".col-md-3").show()
    $(".menu").hide()
  }
  $(window).resize(function(){
    screen_width = $(window).width()
    if(screen_width<770){
      $(".col-md-2").hide()
      $(".col-md-3").hide()
      $(".menu").slideDown(500)
      $(".bussinesses").css({'width':'100%'})
      $(".card").css({'width':'100%'})
      // $(".navigation").css({'width':'100%'})
    }else{
      $(".card").css({'width':'80%'})
      $(".col-md-2").show()
      $(".col-md-3").show()
      $(".menu").hide()
    }
  })
  $(".show-posts").click(function(){
      if(screen_width<770){
        $(".bussinesses").hide()
        $(".bussinesses").css({'width':'100%'})
        $(".emergency").hide()
        $(".posts-all").slideDown(100)
        $(".col-md-2").slideUp(200)
      }else{
        $(".bussinesses").hide()
        $(".emergency").hide()
        $(".posts-all").slideDown(500)
      }

  })
  $(".show-bussinesses").click(function(){
    if(screen_width<770){
      $(".posts-all").hide()
      $(".emergency").hide()
      $(".bussinesses").slideDown(100)
      $(".col-md-2").slideUp(200)
    }else{
    $(".emergency").hide()
    $(".posts-all").hide()
    $(".bussinesses").slideDown(500)
  }
  })
  $(".show-emergency").click(function(){
    if(screen_width<770){
      $(".posts-all").hide()
      $(".bussinesses").hide()
      $(".emergency").slideDown(100)
      $(".col-md-2").slideUp(200)
    }else{
    $(".bussinesses").hide()
    $(".posts-all").hide()
    $(".emergency").slideDown(500)
  }
  })
  $(".menu").click(function(){
    $(".col-md-2").slideDown(500)
    $(".shut").show()
  })
  $(".shut").click(function(){
    $(".col-md-2").slideUp(500)
    $(".shut").hide()
  })
})
// posts
// bussinesses
// emergency
