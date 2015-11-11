
$(document).ready(function() {   
    var as = $("td > a");
    as.click(function(){
    	var aNode = $(this);
    	var tds = aNode.parents("td");
    	var trs = tds.parents("tr");
    	var str = $(trs).attr("class");
		var ids;
		var trids;
		var trNodes;
		if (str.indexOf("_apiheader")>=0)
		{
			ids = str.split("_");
			trids = "case".concat(ids[0]);
			trids = trids.concat("-");
            trs = $("tr");
	        trNodes=trs.length;
	        for (var i=0; i<trNodes; i++){
    	        trNode = trs[i];
    	        str = $(trNode).attr("class");
    	        ids = str.indexOf(trids);
    	        if (ids >= 0){
			        $(trNode).show();
		        }
	        }
    
		}
		if (str.indexOf("_cheader")>=0)
		{
			ids = str.split("_");
			trids =ids[0].concat("_content");
    	    trNodes = $(".".concat(trids));
    	    trNodes.toggle(); 
		}	
    });
});

function Expand_All(){
	var trs = $("tr");
	var trNodes=trs.length;
	var trNode;
	var str;
	var ids;
	for (var i=0; i<trNodes; i++){
    	trNode = trs[i];
    	str = $(trNode).attr("class");
    	ids = str.indexOf("case");
    	if (ids >= 0){
			$(trNode).show();
		}
	}
}

function Expand_Header(){
	var trs = $("tr");
	var trNodes=trs.length;
	var trNode;
	var str;
	var ids;
	for (var i=0; i<trNodes; i++){
    	trNode = trs[i];
    	str = $(trNode).attr("class");
    	ids = str.indexOf("_cheader");
    	if (ids >= 0){
			$(trNode).show();
		}
	}
}

function Collapse_All(){
	window.location.reload();
}
