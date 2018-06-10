//This is a comment.

/*
This is also a comment.
*/

var myHeading=document.querySelector('h2');
myHeading.textContent='Hello,world!';

/*
document.querySelector('html').onclick=function (){
	alert("You click once.");
}
*/

var the_img=document.querySelector('img');

the_img.onclick=function (){
	var the_src=the_img.getAttribute('src');
	
	if(the_src==='images/001.jpg'){
		the_img.setAttribute('src','images/002.jpg');
	}else{
		the_img.setAttribute('src','images/001.jpg');
	}

}

var the_btn=document.querySelector('button');
var the_heading=document.querySelector('h2');

function set_user_name(){
	var user_name=prompt('Please enter your name.');
	
	localStorage.setItem('user_name',user_name);
	the_heading.textContent='Hello, '+user_name+'.'
}

the_btn.onclick=set_user_name;

var user_name=localStorage.getItem('user_name');
if (user_name) {
	the_heading.textContent='Hello, '+user_name+'.'
}else {
	set_user_name();
}

