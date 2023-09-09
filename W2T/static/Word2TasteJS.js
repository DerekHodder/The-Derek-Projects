/*
-----------------------------------------------
W2T/static/Word2TasteJS.js
Derek Stephens
2023 September 9
-----------------------------------------------
*/

const csrf = document.cookie.substring(10);

var outputHeader = document.getElementById("outputheader");
var outputList = document.getElementById("outputlist");

document.getElementById("submitbutton").onclick = function () {
	var inputWord = document.getElementById("inputbox").value;
	$.ajax({
		type: "POST",
		datatype: "json",
		data: {
			"csrfmiddlewaretoken": csrf,
			"word": inputWord,
		},
		success: function (data) {
			console.log(data);
			outputList.innerHTML = "";
			if (Object.keys(data).length == 0) {
				outputHeader.innerHTML = "\"" + inputWord + "\" returned no results!"
			} else {
				outputHeader.innerHTML = "\"" + inputWord + "\" is equivalent to:"
				for (var ingredient in data) {
					var listItem = document.createElement("li");
					listItem.innerText = data[ingredient].toFixed(2) + "% " + ingredient;
					outputList.appendChild(listItem);
				}
			}
		},
		failure: function (data) {
			alert("Something went wrong!");
		}
	});
}