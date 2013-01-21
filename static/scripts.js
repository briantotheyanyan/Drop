function getLocation()
  {
  if (navigator.geolocation)
    {
    navigator.geolocation.getCurrentPosition(showPosition);
    }
  else{x.innerHTML="Geolocation is not supported by this browser.";}
  }
function showPosition(position)
  {
document.getElementById("Latitude").value  =  position.coords.latitude;
document.getElementById("Longitude").value =  position.coords.longitude;
 }



$(document).ready(function() {

       getLocation();
})

