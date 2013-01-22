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

