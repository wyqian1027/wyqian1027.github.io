var shapeDisplayControl = document.querySelector("#display-shapeRecog-control");
var shapeDisplayDiv = document.querySelector("#display-shapeRecog");

shapeDisplayControl.addEventListener("click", function(){
    if (shapeDisplayDiv.style.display == "none"){
        shapeDisplayDiv.setAttribute("style", "display: block");
        shapeDisplayControl.innerHTML = "Hide results";
    } else {
        shapeDisplayDiv.setAttribute("style", "display: none");
        shapeDisplayControl.innerHTML = "Show results";
    }
})