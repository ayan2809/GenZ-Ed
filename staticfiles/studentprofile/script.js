
$(".hamburger .hamburger__inner").click(function(){
  $(".wrapper").toggleClass("active")
})

$(".top_navbar .fas").click(function(){
  
   $(".profile_dd").toggleClass("active");
});


var btn1=document.getElementById("profileButton");
var btn2 = document.getElementById("classesButton");
var btn3 = document.getElementById("chatbotButton");
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

// function getScrollHeight(elm){
//   var savedValue = elm.value
//   elm.value = ''
//   elm._baseScrollHeight = elm.scrollHeight
//   elm.value = savedValue
// }

// function onExpandableTextareaInput({ target:elm }){
//   // make sure the input event originated from a textarea and it's desired to be auto-expandable
//   if( !elm.classList.contains('autoExpand') || !elm.nodeName == 'TEXTAREA' ) return
  
//   var minRows = elm.getAttribute('data-min-rows')|0, rows;
//   !elm._baseScrollHeight && getScrollHeight(elm)

//   elm.rows = minRows
//   rows = Math.ceil((elm.scrollHeight - elm._baseScrollHeight) / 16)
//   elm.rows = minRows + rows
// }


// global delegated event listener
// document.addEventListener('retrievedText', onExpandableTextareaInput)

// document.addEventListener('summarizedText', onExpandableTextareaInput)


// var ROW_HEIGHT = 24; // font-size + lineheight
// var scrollTop, offsetH;
// var els = document.getElementsByTagName('retrievedText');
// 	for (var i = 0; i < els.length; i++){
// 		els[i].style.height = 'auto';
// 		els[i].style.overflow = 'hidden';
// 		els[i].style.height = els[i].scrollHeight - ROW_HEIGHT + "px";
// 		els[i].addEventListener('input', fit, false);
// 	}
// 	function fit(){
// 		while(this.scrollHeight <= this.offsetHeight && this.offsetHeight > ROW_HEIGHT){
// 			this.style.height = this.offsetHeight - ROW_HEIGHT + "px";
// 		}
// 		this.style.height = this.scrollHeight + "px";
// 	}
