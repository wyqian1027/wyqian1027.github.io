var canvas = document.getElementById("myCanvas");;
var ctx = canvas.getContext("2d");;
var CANVAS_HEIGHT = canvas.height;
var CANVAS_WIDTH = canvas.width;
var SCALER_X = 100;
var SCALER_Y = 100;
var zoominBtn = document.querySelector("#zoom-in");
var zoomoutBtn = document.querySelector("#zoom-out");
var periodInput = document.querySelector("#period");
var amplitudeInput = document.querySelector("#amplitude");
var phaseInput = document.querySelector("#phase");
var sourceInput = document.querySelector("#source");
var directionInputs = document.querySelectorAll(".direction");
var inputListeners = [periodInput, amplitudeInput, phaseInput, sourceInput, directionInputs[0], directionInputs[1]];

inputListeners.forEach(function(el){
   el.addEventListener("input", function(el){
    redraw();  
   });
});

zoominBtn.addEventListener("click", function(){
    if (SCALER_X >= 400) return;
    SCALER_X *= 2;
    SCALER_Y *= 2;
    redraw()
})

zoomoutBtn.addEventListener("click", function(){
    if (SCALER_X <= 25) return;
    SCALER_X /= 2;
    SCALER_Y /= 2;
    redraw()
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
    ctx.fillText("x", 22, 30); 
    
    ctx.moveTo(CANVAS_WIDTH-15, CANVAS_HEIGHT/2-10);
    ctx.lineTo(CANVAS_WIDTH,CANVAS_HEIGHT/2);
    ctx.lineTo(CANVAS_WIDTH-15,CANVAS_HEIGHT/2+10);
    ctx.moveTo(CANVAS_WIDTH,CANVAS_HEIGHT/2);
    ctx.lineTo(CANVAS_WIDTH-10,CANVAS_HEIGHT/2)
    ctx.fillText("t", CANVAS_WIDTH-25, CANVAS_HEIGHT/2+27);     
    ctx.stroke();
    ctx.closePath();
    console.log("Coordinates terminated")
}


function drawWave(source, period, amplitude, phase, direction="right", color='#000000'){
    var incr = (direction == 'right' ? 1 : -1)*period;
    amplitude = Math.min(amplitude, CANVAS_HEIGHT/2);
    phase = (phase % 360)*Math.PI/180;
    source = source*SCALER_X + 50;
    ctx.beginPath();
    ctx.fillStyle = color;
    ctx.arc(source, CANVAS_HEIGHT/2, 5, 0, Math.PI*2, true);
    ctx.fill();
    ctx.moveTo(source, CANVAS_HEIGHT/2 + Math.sin(phase)*amplitude*SCALER_Y);
    
    for(var x=source; 0<=x && x<=CANVAS_WIDTH; x+= incr){
        // sin(wt+phi)
        var y = CANVAS_HEIGHT/2 + Math.sin(Math.PI*2/period*(x-source)/SCALER_X + phase)*amplitude*SCALER_Y;
        ctx.lineTo(x,y);
    }
    ctx.lineWidth = 0.5;
    ctx.strokeStyle = color;
    ctx.stroke();
    ctx.closePath();
    console.log("Sine Wave terminated");
}


function redraw(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    var period = periodInput.value;
    var amplitude = amplitudeInput.value;
    var source = sourceInput.value;
    var direction = (directionInputs[0].checked ? 'left' : 'right');
    var phase = phaseInput.value;
    console.log(period, amplitude, source, direction, phase)
    if (period <= 0) {
        period = 1;
        periodInput.value = "1";
    }
    if (amplitude < 0) {
        amplitude = -amplitude;
        amplitudeInput.value = amplitude;
    }
    if (source*1.0*SCALER_X+50 < 0 || source*1.0*SCALER_X+50 > CANVAS_WIDTH) {
        source = 0;
        sourceInput.value = source;
    }
    drawCoordinate(50, CANVAS_WIDTH-50);
    drawWave(source, period, amplitude, phase, direction, 'rgba(255, 0, 0)');
    console.log("Redraw terminated");

}

window.onload = function() {
    SCALER_X = 100;
    SCALER_Y = 100;
    redraw();

};