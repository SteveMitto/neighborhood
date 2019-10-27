$(document).ready(function(){
  $(document).ajaxStart(function(){
    console.log('started');
  })

  $(document).ajaxStop(function(){
    console.log('stoped');
  })
  console.log('ready');

  $("#i_will").click(function(){
    console.log("i will");
    $.ajax({
      method:'GET',
      url:'/setup/bussines_type',
      data:{
        'set':true
      },
      success:function(data){
        console.log(data);
        $(".dis1").hide()
        $(".dis2").slideDown(500)
      }
    })
  $(".dis1").hide()
  $(".dis2").slideDown(500)

  })
  $("#i_wont").click(function(){
    console.log("i wont");
    $.ajax({
      method:'GET',
      url:'/setup/bussines_type',
      data:{
        'set':false
      },
      success:function(data){
        console.log(data);
        $(".dis1").hide()
        $(".dis2").slideDown(500)
      }
    })
    $(".dis1").hide()
    $(".dis2").slideDown(500)

  })
  $("#id_profile_pic").change(function(){
     var item=$("#id_profile_pic").val()
     act = item.split("\\")
    $("#image").text(act[act.length-1]);
  })
  $("#profile").on('submit',function(event){
    var dp =$("#dp").val()
    var act_name = dp.split("\\")
    var final = act_name[act_name.length-1]
    var display_name=$("#display_name") .val()
    var phone_number=$("#phone_number").val()
    var email=$("#email").val()
    $("#profile").ajaxForm({
      method:"GET",
      url:'/update_profile/',
    })
    //   data:{
    //     "dp":dp,
    //     "display_name":display_name,
    //     "phone_number":phone_number,
    //     "email":email
    // },
      // statusCode:{
      //   404:function(error){
      //     console.log(error);
      //   },
      //   500:function(error){
      //     console.log(error);
      //   }
      // },
      // success:function(data) {
      //     console.log(data);
      // }
    // .done(function(data){
    //   console.log(data);
    // })
    event.preventDefault()
  })

  // $("#profile").ajaxSubmit({
  //   method:"GET",
  //   url:'/update_profile/',
  //   success
  // })
})
// csrfmiddlewaretoken
