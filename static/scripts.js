function getLocation(){
	document.getElementById("Latitude").value  =  0;
	document.getElementById("Longitude").value =  0;
}
function showPosition(position){
	document.getElementById("Latitude").value  =  position.coords.latitude;
	document.getElementById("Longitude").value =  position.coords.longitude;
}

