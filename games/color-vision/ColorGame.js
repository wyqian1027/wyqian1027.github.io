// string space careful
var mode = 25;
var hardness = 40;
var r, g, b;
var score;
var clickBlock = false;
// var newr, newg, newb;
var colors = [];//generateRandomColors(mode);
var pickedColor;
var squares = document.querySelectorAll(".square");
var scoreDisplay = document.getElementById("scoreDisplay");
var messageDisplay = document.querySelector("#message");
var h1 = document.querySelector("h1");
var resetButton = document.querySelector("#reset");
// var easyBtn = document.querySelector("#easyBtn");
// var hardBtn = document.querySelector("#hardBtn");
var modeBtns = document.querySelectorAll(".mode");

//main:
init();

resetButton.addEventListener("click", function(){
	reset(true);
});


//predefined functions:
function init(){
	// mode button listeners
	for(var i=0; i<modeBtns.length; i++){
		modeBtns[i].addEventListener("click", function(){
			modeBtns[0].classList.remove("selected");
			modeBtns[1].classList.remove("selected");
			this.classList.add("selected");
			this.textContent === "Easy" ? hardness = 40: hardness = 15;
			reset(true);
		});
	}	
	// square listeners
	for(var i=0; i<squares.length; i++) {
		// add click listeners to squares
		squares[i].addEventListener("click", function(){
			var clickedColor = this.style.backgroundColor;
			if(clickedColor === pickedColor && !clickBlock) {
				messageDisplay.textContent = "Correct!";
				// resetButton.textContent = "Play Again?";
				changeColors(clickedColor);
				clickBlock = true;
				h1.style.backgroundColor = clickedColor;
				setTimeout(reset,1000, false);
			} else {
				if(!clickBlock){
					score = 0;
					scoreDisplay.textContent = score.toString();	
					this.style.backgroundColor = "#232323";
					messageDisplay.textContent = "Try Again!";
				} else {
					messageDisplay.textContent = "Please wait...";					
				}
			}
		});
	}
	reset(true);
}

function reset(changeScore){
	colors = generateRandomColors(mode);
	//pick a new random color from array
	pickedColor	= pickColor();
	//change colorDisplay to match picked Color
	if(changeScore){
		score = 0;
		scoreDisplay.textContent = "0";
	}
	clickBlock = false;
	//change colors of squares
	for(var i=0; i<squares.length; i++) {
		if(colors[i]){
			squares[i].style.display = "block";
			squares[i].style.backgroundColor = colors[i];
		} else {
			squares[i].style.display = "none";
		}	
	}
	h1.style.backgroundColor = "steelblue";
	messageDisplay.textContent = "";
	resetButton.textContent = "New Game";
}

function changeColors(color){
	for(var i=0; i<squares.length; i++){
		squares[i].style.backgroundColor = color;
	}
	score += 100;
	scoreDisplay.textContent = score.toString();
}

//can be modified to make games harder
function pickColor(){
	var randomPosition = Math.floor(Math.random()*colors.length);
	//easy mode, each rgb difference = 50:
	var newr = decider(r, hardness);
	var newg = decider(g, hardness);
	var newb = decider(b, hardness);
	var specialColor = "rgb("+newr+ ", "+newg+", "+newb+")";
	//return:
	colors[randomPosition] = specialColor;
	return specialColor;
}

function generateRandomColors(num){
	var arr = [];
	var defaultColor = randomColor();
	for(i=0; i<num; i++){
		arr.push(defaultColor);
	}
	return arr;
}

function randomColor(){
	r = Math.floor(Math.random()*246)+10;
	g = Math.floor(Math.random()*246)+10;
	b = Math.floor(Math.random()*246)+10;
	return "rgb("+r+ ", "+g+", "+b+")";
}

function decider(value, diff){
	if(Math.floor(Math.random()*2) === 0){
		if(value + diff < 256){
			return value + diff;
		} else {
			return value - diff;
		}
	} else {
		if(value - diff >= 0){
			return value - diff;
		} else {
			return value + diff;
		}
	}

}


