var inputBox = document.querySelector('#input');
var viewBtn = document.querySelector('#view-btn');
var saveBtn = document.querySelector('#save-btn');
var loadBtn = document.querySelector('#load-btn');
var outputBox = document.querySelector('#output');
var delimiterInput = document.querySelector('#delimiter');
var inputArrayName = document.querySelector('#array-id');
var rowNum = document.querySelector('#row-num');
var colNum = document.querySelector('#col-num');
var info = document.querySelector('#info');
var savedList = document.querySelector('#savedList');
var elementSize = document.querySelector('#element-size');

var state;

LoadSample();
init();
setArrayName(getDate());


//display rowblock
function rowBlock(row, rowNum){
    var delimiter = delimiterInput.value;
    if (delimiter.length >0){
        delimiter = delimiter.replace(/ /g, '&nbsp;');
        delimiter = "<li>"+delimiter+"</li>";
    } else {
    // delimiter = '<li class="element ele-row-'+rowNum+'">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</li>';
        delimiter = "<li >&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</li>";
    }
    
    var out ="";
    for (var i=0; i<row.length; i++){
        var el = row[i].replace(/"/g, '');
        el = el.slice(0, parseInt(elementSize.value));
        var elStyle = '<li class="element ele-row-'+rowNum+' ele-col-'+i+'">'+el+'</li>';
        if (i==0) {
            out = out + elStyle;
        } else {
            // out = out+" &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;"+row[i];
            // out = out+" &nbsp;"+row[i].replace(/"/g, '');
            // out = out+""+el;
            out = out+delimiter+elStyle;
        }
    }

    return out;
}

function selectRowOrCol(row, col){
	var children = outputBox.children;
	for (var i=0; i<children.length; i++){
		if (children[i].classList.contains("ele-row-"+row)){
			children[i].classList.add("selected");
		}
		if (children[i].classList.contains("ele-col-"+col)){
			children[i].classList.add("selected");
		}
	}
} 

function unselectRowOrCol(row, col){
	var children = outputBox.children;
	for (var i=0; i<children.length; i++){
		if (children[i].classList.contains("ele-row-"+row)){
			children[i].classList.remove("selected");
		}
		if (children[i].classList.contains("ele-col-"+col)){
			children[i].classList.remove("selected");
		}
	}
} 

//PYTHON:
// [[1, 2, 3], [3,4,5], [5,6, 7]]
function viewPython(str, output){
    // var newStr = str.replace(/(^\s+|\s+$)/g,'');
    var newStr = str.replace(/\s+/g, '');
    newStr = newStr.substring(2, newStr.length-2).split("],[");

    var out = "";
    // console.log("ROW ARR = ", newStr)

    for (var i=0; i<newStr.length; i++){
        out += "<br>";
        var row = newStr[i].split(",");
        // console.log("row ", i, ": ", row);
        out = out + rowBlock(row, i);
    }
    output.innerHTML = out;
}


//EventListener:
viewBtn.addEventListener("click", function(){
	init();
});

saveBtn.addEventListener("click", function(){	
	saveToLocal();
	init();
});

// loadBtn.addEventListener("click", function(){
// 	loadFromLocal();
// 	init();
// });

outputBox.addEventListener("mouseover", function(el){
	
	if (el.target.classList.contains('element')){
		unselectRowOrCol(state[0], state[1]);
		var classValue = el.target.classList.value;
		var r = getIndex(classValue, "row");
		var c = getIndex(classValue, "col");
		selectRowOrCol(r, c);
		displayNumber(r, c);
		state = [r, c];
		// console.log(getIndex(classValue, "row"), getIndex(classValue, "col"))
	}
});

savedList.addEventListener("click", function(el){

	if (el.target.classList.contains('saved-item')){
		console.log(el.target.innerHTML);
		setArrayName(el.target.innerHTML);
		loadFromLocal();
		init();
	}
});


// outputBox.addEventListener("mouseout", function(el){
// 	if (el.target.classList.contains('element')){
// 		var classValue = el.target.classList.value;
// 		unselectRowOrCol(getIndex(classValue, "row"), getIndex(classValue, "col"));
// 	}
// });



function init(){
	state = [0, 0];
	var str = inputBox.value;
	viewPython(str, outputBox);
	selectRowOrCol(state[0], state[1]);
	displayNumber(state[0], state[1]);
	displaySavedList();
}

//functions
function getDate(){
	var d = new Date();
	var date = d.getFullYear()+"-"+(parseInt(d.getMonth())+1)+"-"+d.getDate();
	return date;
}

function saveToLocal() {
	localStorage.setItem(getCurrentName(), getCurrentArray());
}


function loadFromLocal(arrayID) {
	inputBox.value = localStorage.getItem(getCurrentName());
}

function getIndex(classValue, type){

	var ind = classValue.indexOf("ele-"+type)+8;
	var val = 0;
	while (classValue[ind] != " " && ind < classValue.length){
		val += parseInt(classValue[ind]);
		ind += 1;
	}
	return val;
}

function getCurrentArray(){
	return inputBox.value;
}

function getCurrentName(){
	return inputArrayName.value;
}

function setArrayName(name){
	inputArrayName.value = name;
}

function displayNumber(r, c){
	rowNum.innerHTML = r;
	colNum.innerHTML = c;
}

function displaySavedList(){
	var out = "";
	for (var i=0; i< localStorage.length; i++){
		out = out + '<a class="saved-item">'+localStorage.key(i)+'</a>';
	}
	savedList.innerHTML = out;
}

function LoadSample(){
	localStorage["numpy-random-arr"] = "[[0.135, 0.680, 0.374, 0.672, 0.146, 0.719, 0.467, 0.043, 0.640, 0.544], [0.668, 0.424, 0.989, 0.337, 0.030, 0.570, 0.272, 0.220, 0.334, 0.403], [0.008, 0.693, 0.753, 0.328, 0.790, 0.967, 0.468, 0.046, 0.897, 0.703], [0.408, 0.457, 0.644, 0.932, 0.681, 0.614, 0.560, 0.474, 0.220, 0.125], [0.784, 0.933, 0.429, 0.144, 0.389, 0.976, 0.123, 0.152, 0.993, 0.127], [0.351, 0.390, 0.793, 0.638, 0.277, 0.179, 0.472, 0.355, 0.661, 0.766], [0.979, 0.400, 0.699, 0.389, 0.046, 0.106, 0.669, 0.797, 0.675, 0.551], [0.844, 0.136, 0.163, 0.955, 0.050, 0.924, 0.728, 0.887, 0.109, 0.906], [0.268, 0.681, 0.885, 0.109, 0.557, 0.312, 0.734, 0.131, 0.374, 0.031], [0.965, 0.908, 0.574, 0.366, 0.965, 0.153, 0.983, 0.143, 0.135, 0.975]]";
	localStorage["coffee-around-me"] = "[[☕, ☕, ☕, ☕, ☕], [☕, ☕, ☕, ☕, ☕], [☕, ☕, 😂, ☕, ☕], [☕, ☕, ☕, ☕, ☕], [☕, ☕, ☕, ☕, ☕]]";
	localStorage["simple-arr"] = "[[1,2,3],[4,3,5]]";
}