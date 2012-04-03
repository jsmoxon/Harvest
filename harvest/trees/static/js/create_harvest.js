var estimate = 0;

//makes a simple estimate of the harvest based on last years harvest
function estimate_harvest(id, pounds){
    if(document.getElementById(id).checked) {
	estimate = estimate + pounds;
	document.getElementById("pounds").innerHTML = "Estimated Harvest Size: "+estimate+" lbs";
    } else {
	estimate = estimate - pounds;
	document.getElementById("pounds").innerHTML = "Estimated Harvest Size: "+estimate+" lbs";
    }
}