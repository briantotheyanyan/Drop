$(".page").hide();


var browser1 = document.getElementById("browse");
var browser2 = document.getElementById("account");
var browser3 = document.getElementById("drop");

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
	$("body").css("background-image", "url(images/map.jpg)");
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
	$("body").css("background-image", "url(images/browsemap.jpg)");
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
	    	$("body").css("background-image", "url(images/accmap.jpg)");
		$(".page").hide();
		$("#account").show(1500);
	}
);
$("#clearem").click(
    function(){
	$("#txtarea").val('');
});

function hideAddressBar(){
  if(document.documentElement.scrollHeight<window.outerHeight/window.devicePixelRatio)
    document.documentElement.style.height=(window.outerHeight/window.devicePixelRatio)+'px';
  setTimeout(window.scrollTo(window.pageXOffset,1),10);
}
window.addEventListener("load",function(){hideAddressBar();});
window.addEventListener("orientationchange",function(){hideAddressBar();});
window.addEventListener("orientationchange",function(){changeCSS();});

$(window).scroll(function(){                                         
        if ($(window).scrollTop() == 0)    	{window.scrollTo(window.pageXOffset,1)}
    })
    
function changeCSS(){
	        if (window.orientation === undefined) { // desktop
	        	return;
            	}
       
            	if (Math.abs(window.orientation) == 90) { // horizontal
            		browser1.style.width = "100%";
            		browser2.style.width = "100%";
            		browser3.style.width = "100%";
            	}
            	else { // vertical
            		browser1.style.width = "150%";
            		browser2.style.width = "150%";
            		browser3.style.width = "150%";
            	}

}


   
