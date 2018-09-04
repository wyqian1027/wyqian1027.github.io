var h2items = document.querySelectorAll("h2");
var info = document.querySelector("h2 + div");
var bulletpoints = document.querySelectorAll("h2 + ul");


// some hovering effects
for (var i = 0; i<h2items.length; i++) {
	h2items[i].addEventListener("mouseover", function(){
		this.classList.add("h2hover");
	});
	h2items[i].addEventListener("mouseout", function(){
		this.classList.remove("h2hover");
	});
}

// Too mcuh.... 08-25-2018
// info.addEventListener("mouseover", function(){
// 	this.classList.add("ulhover");
// });
// info.addEventListener("mouseout", function(){
// 	this.classList.remove("ulhover");
// });


// for (var i = 0; i<bulletpoints.length; i++) {
// 	bulletpoints[i].addEventListener("mouseover", function(){
// 		this.classList.add("ulhover");
// 	});
// 	bulletpoints[i].addEventListener("mouseout", function(){
// 		this.classList.remove("ulhover");
// 	});
// }