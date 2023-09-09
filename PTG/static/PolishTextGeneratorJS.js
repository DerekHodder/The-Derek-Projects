/*
-----------------------------------------------
PTG/static/PolishTextGeneratorJS.js
Derek Stephens
2023 September 9
-----------------------------------------------
*/

const csrf = document.cookie.substring(10);

function setNewWindow() {
	if (window.innerWidth < 350) {
		document.getElementById("lengthmin").innerHTML = "1";
		document.getElementById("lengthmax").innerHTML = "50";
	} else {
		document.getElementById("lengthmin").innerHTML = "1 Word";
		document.getElementById("lengthmax").innerHTML = "50 Words";
	}
	if (window.innerWidth < 1000) {
		document.getElementById("complexitymin").innerHTML = "S";
		document.getElementById("complexitymedium").innerHTML = "M";
		document.getElementById("complexitymax").innerHTML = "C";
	} else {
		document.getElementById("complexitymin").innerHTML = "Simple";
		document.getElementById("complexitymedium").innerHTML = "Medium";
		document.getElementById("complexitymax").innerHTML = "Complex";
	}
}

$(window).resize(function() {
	setNewWindow();
});

setNewWindow();

document.getElementById("submitbutton").onclick = function() {
	$.ajax({
		type: "POST",
		datatype: "json",
		data: {
			"csrfmiddlewaretoken": csrf,
			"length": document.getElementById("lengthslider").value,
			"complexity": document.getElementById("complexityslider").value,
		},
		success: function(data) {
			document.getElementById("outputtext").innerHTML = data["paragraph"];
		},
		failure: function(data) { 
			alert("Something went wrong!");
		}
	});
}