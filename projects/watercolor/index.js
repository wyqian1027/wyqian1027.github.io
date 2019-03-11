var rbgInputs = document.querySelectorAll(".rgb-input");
var colorBoxes = document.querySelectorAll(".color-box");
var redValues = document.querySelectorAll(".red-value");
var greenValues = document.querySelectorAll(".green-value");
var blueValues = document.querySelectorAll(".blue-value");
var setBtns = document.querySelectorAll(".set-btn");

var mixBtn = document.querySelector("#mix-btn");

var mixBox = document.querySelector("#mix-box");
var mixLabel = document.querySelector("#mix-label");
var mixBox2 = document.querySelector("#mix-box-2");
var mixLabel2 = document.querySelector("#mix-label-2");

var randomBtn = document.querySelector("#random-btn");
var squares = document.querySelectorAll(".square");
var chartLabel = document.querySelector("#chart-label");

var chartBtn1 = document.querySelector("#toggle-chart-btn1");
var chartBtn2 = document.querySelector("#toggle-chart-btn2");
var chartBtns = document.querySelectorAll(".chart-toggle");

//Adobe RGB (1998)
//http://brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html
//RGB to XYZ matrix
var MATRIX = [
    [0.5767309, 0.1855540, 0.1881852], 
    [0.2973769, 0.6273491, 0.0752741], 
    [0.0270343, 0.0706872, 0.9911085]   
];

//XYZ to RGB inverse matrix
var INVERSE = [
    [2.0413690, -0.5649464, -0.3446944], 
    [-0.9692660, 1.8760108, 0.0415560], 
    [ 0.0134474, -0.1183897, 1.0154096]   
];

var chartTheory;
//init:
init();


//color theory:
//1-CMYK:


//mixing-chart:
function setChart(colorArr){
    for(var row=0; row<8; row++){
        for(var col=0; col<8; col++){
            var index = row*8+col;
            var mixColor = CMYKmix(colorArr[col], colorArr[row]);
            drawColor(squares[index], mixColor);
        }
    }
}

function setChartByNeighborArrs(){
    var colorArr1 = getNeighborColorArr(getBoxValues()[0], 7);
    var colorArr2 = getNeighborColorArr(getBoxValues()[1], 7);
    for(var row=0; row<8; row++){
        for(var col=0; col<8; col++){
            var index = row*8+col;
            if (row ==0 && col==0) {
                continue;
            } else if (row==0){
                drawColor(squares[index], colorArr1[col-1]);
            } else if (col==0){
                drawColor(squares[index], colorArr2[row-1]);
            } else {
                if (chartTheory==1){
                    var mixColor = CMYKmix(colorArr1[col-1], colorArr2[row-1]);
                } else {
                    var mixColor = XYZmix(colorArr1[col-1], colorArr2[row-1]);
                }
                drawColor(squares[index], mixColor);
            }            
        }
    }
}

function getColorArr(startColor, endColor, slices){
    var colorArr = [];
    slices = slices-1;
    for(var i=0; i<=slices; i++){
        var r = (startColor[0]*(slices-i)+endColor[0]*i)/slices;
        var g = (startColor[1]*(slices-i)+endColor[1]*i)/slices;
        var b = (startColor[2]*(slices-i)+endColor[2]*i)/slices;
        colorArr.push([r, g, b]);
    }
    return colorArr;
}

function getNeighborColorArr(color, slices){
    slices = slices-1;
    var colorArr = [];
    var maxComp = 0;
    for(var i=0; i<color.length; i++) { 
        color[i] = parseInt(color[i]); 
    } 
    for (var i=0; i<3; i++){
        if (color[i]>color[maxComp]) {
            maxComp = i;
        }
    } 
    var pair = [];
    for (var i=0; i<3; i++){
        if (i != maxComp){
            pair.push(color[i]);
        }
    }
    // console.log("pair = ", pair);
    var incre = Math.round((pair[1] - pair[0])/slices);
    for (var i=0; i<=slices; i++){
        if (maxComp==0){
            colorArr.push([color[0], pair[0]+incre*i, pair[1]-incre*i]);
        } else if (maxComp == 1){
            colorArr.push([pair[0]+incre*i, color[1], pair[1]-incre*i]);
        } else {
            colorArr.push([pair[0]+incre*i, pair[1]-incre*i, color[2]]);
        }   
        // console.log(colorArr[colorArr.length-1]);
    }
    return colorArr;
}






//event listeners:
setBtns.forEach(function(el){
    el.addEventListener("click", function(){
        var btnID = (el.innerHTML.split(" ").slice().pop());
        btnID = parseInt(btnID)-1;
        drawColor(colorBoxes[btnID], getBoxValues()[btnID]);
    })
})

mixBtn.addEventListener("click", function(){
    drawAllBoxes();
    // setChart(getColorArr(getBoxValues()[0], getBoxValues()[1], 8));
    setChartByNeighborArrs();
    setFirst();
});

randomBtn.addEventListener("click", function(){
    rbgInputs.forEach(function(el){
        el.value = getRandomRGB();
    });
    drawAllBoxes();
    setChartByNeighborArrs();
    setFirst();
});

squares.forEach(function(el, ind){
    el.addEventListener("mouseover", function(){
        if (ind != 9) {
            squares[9].style.border = "2px solid #FFFFFF";
        } else {
            setFirstColor();
        }
        if (ind != 0) {
            var colorStr = el.style.backgroundColor;
            var colorArr = colorStr.slice(4, colorStr.length-1).split(",");
            chartLabel.innerHTML = `(${colorArr[0]}, ${colorArr[1]}, ${colorArr[2]})`;
        } else {
            chartLabel.innerHTML = "";
        }
    });
});

chartBtns.forEach(function(el){
    el.addEventListener("click", function(){
        chartTheory = parseInt(this.id[this.id.length-1]);
        showChartBtns();
        setChartByNeighborArrs();
        setFirst();
    })
})





//functions:

function init(){
    // rbgInputs.forEach(function(el){
    //     el.value = getRandomRGB();
    // });
    rbgInputs[0].value = "255";
    rbgInputs[1].value = "255";
    rbgInputs[2].value = "0";
    rbgInputs[3].value = "0";
    rbgInputs[4].value = "255";
    rbgInputs[5].value = "255";
    chartTheory = 2;
    
    drawAllBoxes();
    // setChart(getColorArr(getBoxValues()[0], getBoxValues()[1], 8));
    showChartBtns();
    setFirst();
    setChartByNeighborArrs();
}

function setFirst(){
    setFirstColor();
    setFirstLabel();
}
function setFirstColor() {
    squares[9].style.border = "2px solid #000000";
}
function setFirstLabel() {
    if (chartTheory==1){
        chartLabel.innerHTML = mixLabel.innerHTML;
    } else {
        chartLabel.innerHTML = mixLabel2.innerHTML;
    }
}

function getBoxValues(){
    var values = [];
    for (var i=0; i<redValues.length; i++){
        values.push([redValues[i].value, greenValues[i].value, blueValues[i].value]);
    }
    return values;
}

function drawColor(element, color){
    element.style.backgroundColor = "rgb(" + color[0] + "," + color[1] + "," + color[2] + ")"
}

function drawAllBoxes(){
    var colorValues = getBoxValues();
    for (var i=0; i<colorBoxes.length; i++) {
        drawColor(colorBoxes[i], getBoxValues()[i]);
        colorValues.push(getBoxValues()[i]);
    }
    var mixColorValue = CMYKmix(colorValues[0], colorValues[1]);
    mixLabel.innerHTML = `(${mixColorValue[0]}, ${mixColorValue[1]}, ${mixColorValue[2]})`
    drawColor(mixBox, mixColorValue);
    var mixColorValue2 = XYZmix(colorValues[0], colorValues[1]);
    mixLabel2.innerHTML = `(${mixColorValue2[0]}, ${mixColorValue2[1]}, ${mixColorValue2[2]})`
    drawColor(mixBox2, mixColorValue2);
}

function getRandomRGB(){
    return Math.floor(Math.random()*255);
}

function showChartBtns(){
    chartBtn1.classList.remove("chart-toggle-highlight");
    chartBtn2.classList.remove("chart-toggle-highlight");
    if (chartTheory==1){
        chartBtn1.classList.add("chart-toggle-highlight");
    } else {
        chartBtn2.classList.add("chart-toggle-highlight");
    }
}


function RGBtoCMYK(rgbArr){
    var rr = rgbArr[0]/255;
    var gg = rgbArr[1]/255;
    var bb = rgbArr[2]/255;
    var k = 1 - Math.max(rr, gg, bb);
    var c = (1-rr-k)/(1-k);
    var m = (1-gg-k)/(1-k);
    var y = (1-bb-k)/(1-k);
    return [c, m, y, k];
}

function CMYKtoRGB(cmykArr){
    var c = cmykArr[0];
    var m = cmykArr[1];
    var y = cmykArr[2];
    var k = cmykArr[3];
    var r = Math.round(255*(1-c)*(1-k));
    var g = Math.round(255*(1-m)*(1-k));
    var b = Math.round(255*(1-y)*(1-k));
    return [r, g, b];
}

function CMYKmix(rgb1, rgb2){
    var cmyk1 = RGBtoCMYK(rgb1);
    var cmyk2 = RGBtoCMYK(rgb2);
    var mix = [];
    for (var i=0; i<4; i++){
        mix.push(Math.min(1, cmyk1[i]+cmyk2[i]));
    }
    return CMYKtoRGB(mix);
}

function RGBtoXYZ(rgbArr){
    var rr = rgbArr[0]/255;
    var gg = rgbArr[1]/255;
    var bb = rgbArr[2]/255;
    return matrixVectorMult(MATRIX, [rr, gg, bb]);
}

function XYZtoRGB(XYZArr){
    var rgb = matrixVectorMult(INVERSE, [255*XYZArr[0], 255*XYZArr[1], 255*XYZArr[2]]);
    rgb[0] = Math.min(Math.floor(rgb[0]), 255);
    rgb[1] = Math.min(Math.floor(rgb[1]), 255);
    rgb[2] = Math.min(Math.floor(rgb[2]), 255);
    return rgb;
}

function matrixVectorMult(matrix, array){
    var res = [];
    for (var i=0; i<array.length; i++){
        var temp = 0;
        for (var j=0; j<matrix[0].length; j++){
            temp += matrix[i][j]*array[j];
        }
        res.push(temp);
    }
    return res;
}

function XYZmix(rgb1, rgb2){
    var XYZ1 = RGBtoXYZ(rgb1);
    var XYZ2 = RGBtoXYZ(rgb2);

    // var Xmix = XYZ1[0] + XYZ2[0];
    // var Ymix = XYZ1[1] + XYZ2[1];
    // var Zmix = XYZ1[2] + XYZ2[2];
    // var Xmix = Xmix/(Xmix+Ymix+Zmix);
    // var Ymix = Ymix/(Xmix+Ymix+Zmix);
    // var phi =  XYZ1[1] + XYZ2[1];
    // return XYZtoRGB([Xmix, Ymix, phi]);

    var x1 = XYZ1[0]/(XYZ1[0]+XYZ1[1]+XYZ1[2]);
    var x2 = XYZ2[0]/(XYZ2[0]+XYZ2[1]+XYZ2[2]);
    var y1 = XYZ1[1]/(XYZ1[0]+XYZ1[1]+XYZ1[2]);
    var y2 = XYZ2[1]/(XYZ2[0]+XYZ2[1]+XYZ2[2]);
    // var z1 = XYZ1[2]/(XYZ1[0]+XYZ1[1]+XYZ1[2]);
    // var z2 = XYZ2[2]/(XYZ2[0]+XYZ2[1]+XYZ2[2]);
    var xmix = (x1/y1*XYZ1[1] + x2/y2*XYZ2[1])/(XYZ1[1]/y1 + XYZ2[1]/y2);
    var ymix = (XYZ1[1] + XYZ2[1])/(XYZ1[1]/y1 + XYZ2[1]/y2);
    var Ymix = Math.max(XYZ1[1], XYZ2[1]);
    var X = Ymix/ymix*xmix;
    var Z = Ymix/ymix*(1-xmix-ymix);
    return XYZtoRGB([X, Ymix, Z]);



}