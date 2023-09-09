/*
-----------------------------------------------
WAR/static/WarJS.js
Derek Stephens
2023 September 9
-----------------------------------------------
*/

const gridLength = 100;
document.getElementById("battlegrid").style.gridTemplateColumns = "repeat(" + gridLength.toString() + ", 1fr)";
document.getElementById("battlegrid").style.gridTemplateRows = "repeat(" + gridLength.toString() + ", 1fr)";

const speedSlider = document.getElementById("speedslider");
var speed = 1;
speedSlider.onchange = function() {
	/* The max slider value is reserved for a special speed of 10x */
	if (speedSlider.value == 9) {
		speed = 10;
	} else {
		speed = speedSlider.value / 4;
	}
	if (speed == 0) {
		document.getElementById("speedlabel").innerHTML = "Paused";
	} else {
		document.getElementById("speedlabel").innerHTML = speed.toString() + "x Speed";
	}
}

/* Initialize the battle grid */
const battleGrid = document.getElementById("battlegrid");
var greenPixels = [];
var redPixels = [];
for (var row = 0; row < gridLength; row++) {
	for (var column = 0; column < gridLength; column++) {
		var newPixel = document.createElement("div");
		newPixel.className = "gridpixel";
		newPixel.id = row.toString() + "," + column.toString();
		/* Starting red/green split isn't 50/50 because one side
		starting with an advantage is more interesting */
		if (Math.floor(2 * Math.random()) == 0) {
			newPixel.style.backgroundColor = "mediumspringgreen";
			greenPixels.push([row, column]);
		} else {
			newPixel.style.backgroundColor = "crimson";
			redPixels.push([row, column]);
		}
		battleGrid.appendChild(newPixel);
	}
}

function getNeighborPixel(pixel) {
	var row = pixel[0];
	var column = pixel[1];
	var randomNumber;
	var neighborPixel;
	/* 9 cases for the 9 possible positions a pixel can be in
	(4 corners, 4 sides, middle) */
	if (row == 0 && column == 0) {
		randomNumber = Math.floor(2 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row + 1, column];
		} else {
			neighborPixel = [row, column + 1];
		}
	} else if (row == 0 && column == gridLength - 1) {
		randomNumber = Math.floor(2 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row + 1, column];
		} else {
			neighborPixel = [row, column - 1];
		}
	} else if (row == gridLength - 1 && column == 0) {
		randomNumber = Math.floor(2 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row - 1, column];
		} else {
			neighborPixel = [row, column + 1];
		}
	} else if (row == gridLength - 1 && gridLength - 1) {
		randomNumber = Math.floor(2 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row - 1, column];
		} else {
			neighborPixel = [row, column - 1];
		}
	} else if (column == 0) {
		randomNumber = Math.floor(3 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row - 1, column];
		} else if (randomNumber == 1) {
			neighborPixel = [row + 1, column];
		} else {
			neighborPixel = [row, column + 1];
		}
	} else if (row == 0) {
		randomNumber = Math.floor(3 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row, column - 1];
		} else if (randomNumber == 1) {
			neighborPixel = [row, column + 1];
		} else {
			neighborPixel = [row + 1, column];
		}
	} else if (column == gridLength - 1) {
		randomNumber = Math.floor(3 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row - 1, column];
		} else if (randomNumber == 1) {
			neighborPixel = [row + 1, column];
		} else {
			neighborPixel = [row, column - 1];
		}
	} else if (row == gridLength - 1) {
		randomNumber = Math.floor(3 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row, column - 1];
		} else if (randomNumber == 1) {
			neighborPixel = [row, column + 1];
		} else {
			neighborPixel = [row - 1, column];
		}
	} else {
		randomNumber = Math.floor(4 * Math.random());
		if (randomNumber == 0) {
			neighborPixel = [row, column - 1];
		} else if (randomNumber == 1) {
			neighborPixel = [row - 1, column];
		} else if (randomNumber == 2) {
			neighborPixel = [row, column + 1];
		} else {
			neighborPixel = [row + 1, column];
		}
	}
	return neighborPixel;
}

/* All hail StackOverflow */
const includesArray = (data, arr) => {
	return data.some(e => Array.isArray(e) && e.every((o, i) => Object.is(arr[i], o)));
}

/* All hail StackOverflow */
function sleep(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

/* Green and red get 1 turn each until someone runs out of pixels */
const fightButton = document.getElementById("fightbutton");
fightButton.onclick = async function() {
	fightButton.style.display = "none";
	while (greenPixels.length != 0 && redPixels.length != 0) {
		var selectedPixel = greenPixels[Math.floor(greenPixels.length * Math.random())];
		var neighborPixel = getNeighborPixel(selectedPixel);
		/* Probability of a pixel being captured is directly tied to 
		how many neighbors of the opposite color that pixel has*/
		if (includesArray(redPixels, neighborPixel) && speed != 0) {
			/* Remove a pixel from its original color list,
			add it to the oppsite color list, and update the grid */
			greenPixels.splice(greenPixels.indexOf(selectedPixel), 1);
			redPixels.push(selectedPixel);
			document.getElementById(selectedPixel[0].toString() + "," + selectedPixel[1].toString()).style.backgroundColor = "crimson";
		}
		await sleep(100 / speed);
		selectedPixel = redPixels[Math.floor(redPixels.length * Math.random())];
		neighborPixel = getNeighborPixel(selectedPixel);
		if (includesArray(greenPixels, neighborPixel) && speed != 0) {
			redPixels.splice(redPixels.indexOf(selectedPixel), 1);
			greenPixels.push(selectedPixel);
			document.getElementById(selectedPixel[0].toString() + "," + selectedPixel[1].toString()).style.backgroundColor = "mediumspringgreen";
		}
		await sleep(100 / speed);
	}
	if (greenPixels.length == 0) {
		document.getElementById("victorylabel").innerHTML = "Red wins!";
	} else {
		document.getElementById("victorylabel").innerHTML = "Green wins!";
	}
}