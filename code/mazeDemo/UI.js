var CANVAS_WIDTH = 1000;
var CANVAS_HEIGHT = 1000;

var canvas = document.getElementById('canvas');
canvas.width = CANVAS_WIDTH;
canvas.height = CANVAS_HEIGHT;
var ctx = canvas.getContext('2d');

// Canvas Drawing Functions
var drawPoint = function(x, y, color, size) {
    ctx.beginPath();
    ctx.arc(x,y,size,0,2*Math.PI);
    ctx.fillStyle = color;
    ctx.stroke();
    ctx.fillStyle = color;
    ctx.fill();
    ctx.closePath();
};

var drawEdge = function(fromX, fromY, toX, toY, color, size) {
    ctx.lineWidth = size;
    ctx.beginPath();
    ctx.moveTo(fromX, fromY);
    ctx.lineTo(toX, toY);
	ctx.strokeStyle = color;
    ctx.stroke();
    ctx.closePath();
};

var clearCanvas = function(){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

var fillCanvasBackground = function(){
    ctx.fillStyle = BACKGROUND_COLOR;
    ctx.fillRect(0, 0, canvas.width, canvas.height);
}

var displayText = function(text){
    ctx.font = "15px Arial";
    ctx.fillStyle = "white";
    ctx.fillText(text, CANVAS_WIDTH/2-text.length*3, BOUNDARY/2);
}

// specifically for displaying path
var connectPath = function(path, edgeColor, edgeWidth){
    if (path.length == 0) return;
    var [x1, y1] = grid.getCoorfromID(path[0]);
    for (var i = 1; i < path.length; i++){
        var [x2, y2] = grid.getCoorfromID(path[i]);
        drawPoint(x1, y1, edgeColor, POINT_SIZE);
        drawEdge(x1, y1, x2, y2, edgeColor, edgeWidth);
        drawPoint(x2, y2, edgeColor, POINT_SIZE);
        x1 = x2;
        y1 = y2;
    }
}

var displaySolution = function(path){
    if (path == []) return;
    connectPath(path, "red", 5);
    // displayText("path length = " + path.length);
}