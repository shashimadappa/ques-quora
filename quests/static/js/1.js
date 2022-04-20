// alert("Hello, Welcome to Javatpoint");  


let button = document.getElementById("but");
let count = document.getElementById("votes");
let local = 0;
function clicked( ){
    
    
   console.log("clicked");
   local++;
   count.innerHTML = local;
}

 button.addEventListener('click', clicked);



//  function myFunction() {
//    var dots = document.getElementById("dots");
//    var moreText = document.getElementById("more");
//    var btnText = document.getElementById("myBtn");
 
//    if (dots.style.display === "none") {
//      dots.style.display = "inline";
//      btnText.innerHTML = "Read more"; 
//      moreText.style.display = "none";
//    } else {
//      dots.style.display = "none";
//      btnText.innerHTML = "Read less"; 
//      moreText.style.display = "inline";
//    }
//  }