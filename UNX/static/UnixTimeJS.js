/*
-----------------------------------------------
UNX/static/UnixTimeJS.js
Derek Stephens
2023 September 9
-----------------------------------------------
*/

const csrf = document.cookie.substring(10);
const timeDiv = document.getElementById("time");

function displayCategories() {
	timeDiv.innerHTML = Math.floor(Date.now() / 1000).toString();
	$.ajax({
		type: "POST",
		datatype: "json",
		data: {
			"csrfmiddlewaretoken": csrf,
			"time": Math.floor(Date.now() / 1000),
		},
		success: function(data) {
			document.getElementById("list").innerHTML = "";
			for (category in data) {
				var newDiv = document.createElement("li");
				newDiv.innerHTML = category;
				if (data[category] == "green") {
					newDiv.style.color = "green";
				} else {
					newDiv.style.color = "red";
				}
				document.getElementById("list").appendChild(newDiv);
			}
		},
		failure: function(data) { 
			alert("Something went wrong!");
		}
	});
}

/* Interval is 500ms to ensure the correct time
will be displayed at least once per second */
setInterval(displayCategories, 500);