if((Browser.Platform.ios) || (Browser.Platform.android) && (Browser.safari)) {
  //For iPhone and Andriod To remove Address bar when viewing website on Safari Mobile
  // When ready...
  window.addEventListener("load",function() {
    // Set a timeout...
    setTimeout(function(){
    // Hide the address bar!
    window.scrollTo(0, 1);
    }, 0);
  });
}


$(".page").hide();

var newpage = true;
var mapload = true;
$("#dropbutt").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'0px'});
			newpage=false;
		}
		$(".page").hide();
		$("#drop").show();
		getPosition();
	}
);
$("#browsebutt").click(
	function(){		
		if(newpage){
			$("#tbl").animate({top:'0px'});
			newpage=false;
		}
		$(".page").hide();
		$("#browse").show();
		getPosition();
	}
);

$("#mapbutt").click(
	function(){
		if (mapload){
		 	 initialize();
		  	  mapload = false;
		}
		if(newpage){
			$("#tbl").animate({top:'0px'});
			newpage=false;
			
		}
		$(".page").hide();
		$("#map").show();
		       
		  				
	}
);

$("#accountbutt").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'0px'});
			newpage=false;
		}
		$(".page").hide();
		$("#account").show();
	}
);

