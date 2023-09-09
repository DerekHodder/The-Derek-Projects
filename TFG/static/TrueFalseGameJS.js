/*
-----------------------------------------------
TFG/static/TrueFalseGameJS.js
Derek Stephens
2023 September 9
-----------------------------------------------
*/

const csrf = document.cookie.substring(10);

var correct = 0;
var incorrect = 0;
var total;

/* Both these will be corrected to their actual starting values
when switchScoreDisplayMode() and switchGameMode() are called*/
var scoreDisplayMode = "correct-incorrect";
var gameMode = "challenge";

var prompt;
var answer;

function updateScore() {
	total = correct + incorrect;
	var digits = total.toString().length;
	if (scoreDisplayMode == "correct-total") {
		var totalDigits = total.toString().length;
		document.getElementById("score").innerHTML = correct + "\n" + "─".repeat(totalDigits) + "\n" + total;
		/* In case anyone actually plays like 100 rounds */
		document.getElementById("scorecontainer").style.width = (2 + 3 * totalDigits).toString() + "vw";
	} else {
		document.getElementById("score").innerHTML = correct + "─" + incorrect;
		document.getElementById("scorecontainer").style.width = (4 + 3 * correct.toString().length + 3 * incorrect.toString().length).toString() + "vw";
	}
}

function switchScoreDisplayMode() {
	if (scoreDisplayMode == "correct-total") {
		scoreDisplayMode = "correct-incorrect";
	} else {
		scoreDisplayMode = "correct-total";
	}
	updateScore();
}

function switchGameMode() {
	if (gameMode == "normal") {
		gameMode = "challenge";
		document.getElementById("challengemode").innerHTML = "Challenge Mode";
	} else {
		gameMode = "normal";
		document.getElementById("challengemode").innerHTML = "Normal Mode";
	}
	correct = 0;
	incorrect = 0;
	updateScore();
}

function generatePrompt() {
	$.ajax({
		type: "POST",
		datatype: "json",
		data: {
			"csrfmiddlewaretoken": csrf,
			"mode": gameMode,
		},
		success: function(data) {
			prompt = data["prompt"];
			answer = data["answer"];
			document.getElementById("promptdiv").innerHTML = prompt;
		},
		failure: function(data) { 
			alert("Something went wrong!");
		}
	});
}

switchScoreDisplayMode();
switchGameMode();
generatePrompt();

document.getElementById("scorecontainer").onclick = function() {
	switchScoreDisplayMode();
}

document.getElementById("challengemode").onclick = function() {
	switchGameMode();
	generatePrompt();
}

document.getElementById("truebutton").onclick = function() {
	if (answer == "True") {
		correct += 1;
	} else {
		incorrect += 1;
	}
	updateScore();
	generatePrompt();
}

document.getElementById("falsebutton").onclick = function() {
	if (answer == "False") {
		correct += 1;
	} else {
		incorrect += 1;
	}
	updateScore();
	generatePrompt();
}