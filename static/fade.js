var h = 0;
var v = 400;
counter1 = 0; //counts the current diagonal "row"
counter2 = 0; //counts the current position within that row
function step(){
	var c = document.getElementById("canv");
	var ctx = c.getContext("2d");
	ctx.fillStyle="#FFFFFF";
	ctx.fillRect(h,v,50,50);
	
	counter1+=50;
}
function fade(){
	setInterval(step,6);
}

