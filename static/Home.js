$(".page").hide();
var newpage = true;
$("#drop").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'0px'});
			newpage=false;
		}
		$(".page").hide();
		$("#drop").show();
	}
);
$("#browse").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'0px'});
			newpage=false;
		}
		$(".page").hide();
		$("#browse").show();
	}
);

$("#map").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'0px'});
			newpage=false;
		}
		$(".page").hide();
		$("#map").show();
	}
);

$("#account").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'0px'});
			newpage=false;
		}
		$(".page").hide();
		$("#account").show();
	}
);
