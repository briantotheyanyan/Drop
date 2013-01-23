$(".page").hide();




var newpage = true;
var mapload = true;
$("#dropbutt").click(
	function(){
		$(".selection").show();
		$("#dropbutt").hide();
		if(newpage != "drop"){
			$("#tbl").animate({top:'300px', opacity: 'toggle'}).delay(1600).animate({top:'0px', opacity: 'toggle'})
			
			newpage="drop";
		}
		$(".page").hide();
		$("#drop").show(1500);
		
		getPosition();
	}
);
$("#browsebutt").click(
	function(){
		$(".selection").show();
		$("#browsebutt").hide();
		if(newpage != "browse"){
			$("#tbl").animate({top:'300px', opacity: 'toggle'}).delay(1600).animate({top:'0px', opacity: 'toggle'})
			
			newpage="browse";
		}
		$(".page").hide();
		$("#browse").show(1500);
		getPosition();
	}
);

$("#mapbutt").click(
	function(){
		$(".selection").show();
		$("#mapbutt").hide();
		if (mapload){
			 setTimeout(function() {  initialize()}, 1100);
		  	  mapload = false;
		}
		if(newpage != "map"){
			$("#tbl").animate({top:'300px', opacity: 'toggle'}).delay(1600).animate({top:'0px', opacity: 'toggle'})
			newpage="map";
			
		}
		
		$(".page").hide();
		$("#map").show(1000)
		       
		  				
	}
);

$("#accountbutt").click(
	function(){
		$(".selection").show();
		$("#accountbutt").hide();
		if(newpage != "account"){
			$("#tbl").animate({top:'300px', opacity: 'toggle'}).delay(1600).animate({top:'0px', opacity: 'toggle'})
			
			newpage="account";
		}
		$(".page").hide();
		$("#account").show(1500);
	}
);


function hideAddressBar(){
  if(document.documentElement.scrollHeight<window.outerHeight/window.devicePixelRatio)
    document.documentElement.style.height=(window.outerHeight/window.devicePixelRatio)+'px';
  setTimeout(window.scrollTo(1,1),0);
}
window.addEventListener("load",function(){hideAddressBar();});
window.addEventListener("orientationchange",function(){hideAddressBar();});

