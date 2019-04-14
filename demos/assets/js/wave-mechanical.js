var canvas = document.getElementById("myCanvas");;
var ctx = canvas.getContext("2d");;
var CANVAS_HEIGHT = canvas.height;
var CANVAS_WIDTH = canvas.width;
var SCALER_X = 100;
var SCALER_Y = 100;
var zoominBtn = document.querySelector("#zoom-in");
var zoomoutBtn = document.querySelector("#zoom-out");
var runBtn = document.querySelector("#simulate");
var stopBtn = document.querySelector("#stop");
var periodInput = document.querySelector("#period");
var amplitudeInput = document.querySelector("#amplitude");
var wavelengthInput = document.querySelector("#wavelength");
var sourceInput = document.querySelector("#source");
var directionInputs = document.querySelectorAll(".direction");
// var cancelAnimate = false;
var animateID = false;
var startTime;

//default
var period = 1;
var amplitude = 1;
var source = 0;
var direction = 'right';
var wavelength = 1;
var color = "rgba(255, 0, 0)";

zoominBtn.addEventListener("click", function(){
    if (SCALER_X >= 400) return;
    SCALER_X *= 2;
    SCALER_Y *= 2;
})

zoomoutBtn.addEventListener("click", function(){
    if (SCALER_X <= 25) return;
    SCALER_X /= 2;
    SCALER_Y /= 2;
})

function drawCoordinate(x1, x2){
    ctx.beginPath();
    ctx.fillStyle = 'rgba(0, 0, 0)';
    ctx.strokeStyle = 'rgba(0, 0, 0)';
    ctx.font = '15px serif';
    //X coordinate
    for(var x=0; x<CANVAS_WIDTH; x += 10){
        ctx.moveTo(x+5,CANVAS_HEIGHT/2);
        ctx.lineTo(x,CANVAS_HEIGHT/2);
    }
    ctx.stroke();
    var y = CANVAS_HEIGHT/2;
    for (var x=50; x<=CANVAS_WIDTH-50; x+= SCALER_X){
      ctx.rect(x, y-5, 1, 5);
      ctx.fill();
      ctx.fillText((x-50)/SCALER_X, x-3, y+20);        
    }
    //Y coordinate
    for(var y=CANVAS_HEIGHT; y>0; y -= 10){
        ctx.moveTo(50,y);
        ctx.lineTo(50,y-5);
    }
    var x = 50;
    for (var y=CANVAS_HEIGHT/2; y>0; y-= SCALER_Y){
      ctx.rect(x-5, y, 5, 1);
      ctx.fill();
      ctx.fillText(-(y-CANVAS_HEIGHT/2)/SCALER_Y, x-15, y+5);        
    }
    for (var y=CANVAS_HEIGHT/2; y< CANVAS_HEIGHT; y+= SCALER_Y){
      ctx.rect(x-5, y, 5, 1);
      ctx.fill();
      ctx.fillText((y-CANVAS_HEIGHT/2)/SCALER_Y, x-15, y+5);        
    }
    ctx.stroke();
    ctx.closePath();
    
    //Arrows:
    ctx.beginPath();
    ctx.font = '25px serif';
    ctx.lineWidth = 2;
    ctx.moveTo(40,15);
    ctx.lineTo(50,0);
    ctx.lineTo(60,15);
    ctx.moveTo(50,0);
    ctx.lineTo(50,10)
    ctx.fillText("y", 22, 30); 
    
    ctx.moveTo(CANVAS_WIDTH-15, CANVAS_HEIGHT/2-10);
    ctx.lineTo(CANVAS_WIDTH,CANVAS_HEIGHT/2);
    ctx.lineTo(CANVAS_WIDTH-15,CANVAS_HEIGHT/2+10);
    ctx.moveTo(CANVAS_WIDTH,CANVAS_HEIGHT/2);
    ctx.lineTo(CANVAS_WIDTH-10,CANVAS_HEIGHT/2)
    ctx.fillText("x", CANVAS_WIDTH-25, CANVAS_HEIGHT/2+27);     
    ctx.stroke();
    ctx.closePath();
}

function getValues(){
    period = periodInput.value;
    amplitude = amplitudeInput.value;
    source = sourceInput.value;
    direction = (directionInputs[0].checked ? 'left' : 'right');
    wavelength = wavelengthInput.value;
    if (period == 0 || wavelength == 0) return false;
    if (period < 0) {
        period = -period;
        periodInput.value = period;
    }
    if (wavelength < 0) {
        wavelength = - wavelength;
        wavelengthInput.value = wavelength;
    }
    if (amplitude < 0 || amplitude > CANVAS_HEIGHT/2) {
        amplitude = Math.abs(amplitude);
        amplitude = Math.min(amplitude, CANVAS_HEIGHT/2);
        amplitudeInput.value = amplitude;
    }
    if (source*1.0*SCALER_X+50 < 0 || source*1.0*SCALER_X+50 > CANVAS_WIDTH) {
        source = 0;
        sourceInput.value = source;
    }
    source = source*SCALER_X + 50;
    return true;
}

runBtn.addEventListener("click", function(el){
    if (animateID != false) {
        window.cancelAnimationFrame(animateID);
        animateID = false;
    }
    if (getValues() == true){
        startTime = new Date();
        animateID = window.requestAnimationFrame(animateWave);
    }
});

stopBtn.addEventListener("click", function(el){
    window.cancelAnimationFrame(animateID);
    animateID = false;
});


function animateWave(){
    var incr = (direction == 'right' ? 1 : -1)*period;
    var sign = (direction == 'right' ? -1 : 1);
    var deltaTime = ((new Date())- startTime)/1000.0;
    if (deltaTime > 10){
        return;
    }
    ctx.clearRect(0,0,canvas.width,canvas.height);
    drawCoordinate(50, CANVAS_WIDTH-50);

    ctx.beginPath();
    ctx.fillStyle = color;
    ctx.arc(source, CANVAS_HEIGHT/2, 5, 0, Math.PI*2, true);
    ctx.fill();
    ctx.moveTo(source, CANVAS_HEIGHT/2);
    
    for(var x=source; 0<=x && x<=CANVAS_WIDTH; x+= incr){
        // Acos(kx-wt)
        var y = CANVAS_HEIGHT/2 + Math.cos(Math.PI*2/wavelength*(x-source)/SCALER_X + sign*Math.PI*2/period*deltaTime)*amplitude*SCALER_Y;
        ctx.lineTo(x,y);
    }
    ctx.lineWidth = 0.5;
    ctx.strokeStyle = color;
    ctx.stroke();
    ctx.fillText("t = "+deltaTime, CANVAS_WIDTH-100, 0+27);
    ctx.closePath();
    animateID = window.requestAnimationFrame(animateWave);
}


window.onload = function() {
    SCALER_X = 100;
    SCALER_Y = 100;
    drawCoordinate(50, CANVAS_WIDTH-50);

};