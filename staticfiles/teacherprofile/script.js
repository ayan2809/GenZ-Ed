
$(".hamburger .hamburger__inner").click(function(){
  $(".wrapper").toggleClass("active")
})

$(".top_navbar .fas").click(function(){
  
   $(".profile_dd").toggleClass("active");
});


var btn1=document.getElementById("profileButton");
var btn2 = document.getElementById("classesButton");
var btn3 = document.getElementById("materialButton");
var btn4 = document.getElementById("insightsButton");
var btn5 = document.getElementById("settingsButton");
if(btn1!=null){
  btn1.addEventListener("click", function() {
    btn1.className='active';
    btn2.className='';
    btn3.className='';
    btn4.className='';  
    btn5.className='';
    for(var i =1;i<=5;i++){
      document.getElementById("item"+i).style.display = "none";
    }
    document.getElementById("item1").style.display = " block";
  });
}
if(btn2!=null){
  btn2.addEventListener("click", function() {
    btn2.className='active';
    btn1.className='';
    btn3.className='';
    btn4.className='';  
    btn5.className='';
    for(var i =1;i<=5;i++){
      document.getElementById("item"+i).style.display = "none";
    }
    document.getElementById("item2").style.display = " block";
  });
}
if(btn3!=null){
  btn3.addEventListener("click", function() {
    btn3.className='active';
    btn1.className='';
    btn2.className='';
    btn4.className='';  
    btn5.className='';
    for(var i =1;i<=5;i++){
      document.getElementById("item"+i).style.display = "none";
    }
    document.getElementById("item3").style.display = " block";
  });
}
if(btn4!=null){
  btn4.addEventListener("click", function() {
    btn4.className='active';
    btn1.className='';
    btn2.className='';
    btn3.className='';  
    btn5.className='';
    for(var i =1;i<=5;i++){
      document.getElementById("item"+i).style.display = "none";
    }
    document.getElementById("item4").style.display = " block";
  });
}
if(btn5!=null){
  btn5.addEventListener("click", function() {
    btn5.className='active';
    btn1.className='';
    btn2.className='';
    btn3.className='';  
    btn4.className='';
    for(var i =1;i<=5;i++){
      document.getElementById("item"+i).style.display = "none";
    }
    document.getElementById("item5").style.display = " block";
  });
}



// script to retrieve data from database

// var username= document.getElementById("profile_name").innerHTML;
// if(username!=null)
// {
//   console.log(username);
// }



