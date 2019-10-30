$(document).ready(function(){
  console.log('ready');
  $(".show-posts").click(function(){
    $(".bussinesses").hide()
    $(".emergency").hide()
    $(".posts-all").slideDown(500)
  })
  $(".show-bussinesses").click(function(){
    $(".emergency").hide()
    $(".posts-all").hide()
    $(".bussinesses").slideDown(500)
  })
  $(".show-emergency").click(function(){
    $(".bussinesses").hide()
    $(".posts-all").hide()
    $(".emergency").slideDown(500)
  })
})
// posts
// bussinesses
// emergency
