function PreSubmit(form){
	var func=function(){form.submit();}
	setTimeout(func,1000);
}


/*

$$("div").hide();
var newpage = true;
$("#drop").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'-8px'});
			newpage=false;
		}
		$("div").hide();
		$("#Drop").show();
	}
);
$("#browse").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'-8px'});
			newpage=false;
		}
		$("div").hide();
		$("#Browse").show();
	}
);

$("#map").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'-8px'});
			newpage=false;
		}
		$("div").hide();
		$("#Map").show();
	}
);

$("#account").click(
	function(){
		if(newpage){
			$("#tbl").animate({top:'-8px'});
			newpage=false;
		}
		$("div").hide();
		$("#Account").show();
	}
);

*/


