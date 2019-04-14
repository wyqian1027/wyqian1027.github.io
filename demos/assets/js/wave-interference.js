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
var showBtn = document.querySelector("#show");
var periodInput = document.querySelector("#period");
var amplitudeInput = document.querySelector("#amplitude");
var wavelengthInput = document.querySelector("#wavelength");
var source1Input = document.querySelector("#source1");
var source2Input = document.querySelector("#source2");
// var cancelAnimate = false;
var animateID = false;
var state ="";
var startTime;

//default
var period = 2;
var amplitude = 1;
var source1 = 2;
var source2 = 6;
var direction = 'right';
var wavelength = 2;
var color = "rgba(0, 0, 0)";

zoominBtn.addEventListener("click", function(){
    if (SCALER_X >= 400) return;
    SCALER_X *= 2;
    SCALER_Y *= 2;
    if (state == "show" && getValues() == true) showInference();
})

zoomoutBtn.addEventListener("click", function(){
    if (SCALER_X <= 25) return;
    SCALER_X /= 2;
    SCALER_Y /= 2;
    if (state == "show" && getValues() == true) showInference();
})

function drawCoordinate(){
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
    source1 = source1Input.value;
    source2 = source2Input.value;
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
    if (source1*1.0*SCALER_X+50 < 0 || source1*1.0*SCALER_X+50 > CANVAS_WIDTH) {
        source1 = 2.0;
        source1Input.value = source1;
    }
    if (source2*1.0*SCALER_X+50 < 0 || source2*1.0*SCALER_X+50 > CANVAS_WIDTH) {
        source2 = 6.0;
        console.log(source2)
        source2Input.value = source2;
    }
    source1 = source1*SCALER_X + 50;
    source2 = source2*SCALER_X + 50;
    return true;
}

runBtn.addEventListener("click", function(el){
    if (animateID != false) {
        window.cancelAnimationFrame(animateID);
        animateID = false;
    }
    if (getValues() == true){
        state = "run";
        startTime = new Date();
        animateID = window.requestAnimationFrame(animateWave);
    }
    
});

stopBtn.addEventListener("click", function(el){
    window.cancelAnimationFrame(animateID);
    animateID = false;
    state = "stop";
});

showBtn.addEventListener("click", function(el){
    window.cancelAnimationFrame(animateID);
    animateID = false;    
    if (getValues() == true){
        showInference();
    }
    state = "show";
})

function showInference(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.beginPath();
    var cali = 5;
    for(var x=0; x<CANVAS_WIDTH; x+= cali){
        for (var y=0; y<CANVAS_HEIGHT; y += cali){
            var d1 = Math.sqrt((x-source1)**2 + (y-CANVAS_HEIGHT/2)**2);
            var d2 = Math.sqrt((x-source2)**2 + (y-CANVAS_HEIGHT/2)**2);
            var pathDiff = Math.abs(d1-d2)/SCALER_X;
            var frac = pathDiff/wavelength;
            frac = Math.max(0, 1.0-Math.abs(Math.round(frac) - frac)/0.5);
            // var colorCode = `rgb(
            //     255,
            //     ${255-Math.floor(frac*200)},
            //     ${255-Math.floor(frac*200)})`;
            if (frac >= 0.96) {
                ctx.fillStyle = "rgb(255, 20, 20)";
                ctx.fillRect(x, y, cali, cali);

            } else if (frac <= 0.04) {
                ctx.fillStyle = "rgb(20, 20, 255)";
                ctx.fillRect(x, y, cali, cali);

            }
        }
    }
    ctx.lineWidth = 0.5;
    ctx.strokeStyle = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(0,0,0)';
    ctx.stroke();
    ctx.fillText("Interference", CANVAS_WIDTH-200, 0+27);
    ctx.arc(source1, CANVAS_HEIGHT/2, 5, 0, Math.PI*2, true);
    ctx.arc(source2, CANVAS_HEIGHT/2, 5, 0, Math.PI*2, true);
    ctx.fill();
    ctx.closePath();
    drawCoordinate();
}

function animateWave(){
    var deltaTime = ((new Date())- startTime)/1000.0;
    if (deltaTime > 10){
        state = "";
        return;
    }
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.beginPath();
    var timePart = Math.PI*2/period*deltaTime;
    var cali = 5;
    for(var x=0; x<CANVAS_WIDTH; x+= cali){
        for (var y=0; y<CANVAS_HEIGHT; y += cali){
            var d1 = Math.sqrt((x-source1)**2 + (y-CANVAS_HEIGHT/2)**2);
            var d2 = Math.sqrt((x-source2)**2 + (y-CANVAS_HEIGHT/2)**2);
            var combine = (Math.cos(Math.PI*2/wavelength*d1/SCALER_X - timePart) +
            Math.cos(Math.PI*2/wavelength*d2/SCALER_X - timePart)) / 2;
            combine = Math.abs(combine**2);
            var colorCode = `rgb(
                245,
                ${255-Math.floor(combine*200)},
                ${255-Math.floor(combine*200)})`;
            if (combine >= 0.0) {
                ctx.fillStyle = colorCode;
                ctx.fillRect(x, y, cali, cali);
            }
        }
    }
    ctx.lineWidth = 0.5;
    ctx.strokeStyle = 'rgb(0,0,0)';
    ctx.fillStyle = 'rgb(0,0,0)';
    ctx.stroke();
    ctx.fillText("t = "+deltaTime, CANVAS_WIDTH-100, 0+27);
    ctx.arc(source1, CANVAS_HEIGHT/2, 5, 0, Math.PI*2, true);
    ctx.arc(source2, CANVAS_HEIGHT/2, 5, 0, Math.PI*2, true);
    ctx.fill();
    ctx.closePath();
    drawCoordinate();
    animateID = window.requestAnimationFrame(animateWave);
}


window.onload = function() {
    SCALER_X = 100;
    SCALER_Y = 100;
    drawCoordinate();

};