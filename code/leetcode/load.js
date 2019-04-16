
function load(id) {
    httpGet("probs/"+id+"/description.txt", function(textFile){
        pDesp.innerHTML = textFile.split('\n').slice(1).join("<br>");
        pTitle.innerHTML = textFile.split('\n')[0];
    });
    httpGet("probs/"+id+"/explanation.txt", function(textFile){
        if (textFile != ""){
            pExplain.innerHTML = textFile.split('\n').join("<br>");        
        }
    });
    
    // apply PR.prettyPrintOne to dynamically generated text
    httpGet("probs/"+id+"/code-python.txt", function(textFile){
        if (textFile != ""){
            textPython.style.display = "block";
            codePython.innerHTML = PR.prettyPrintOne(textFile, "python3");        
            codePython.style.display = "block";
        } else {
            
        }
    });
    httpGet("probs/"+id+"/code-java.txt", function(textFile){
        if (textFile != ""){
            textJava.style.display = "block";
            codeJava.innerHTML = PR.prettyPrintOne(textFile, "java");   
            codeJava.style.display = "block";
        }
    });
}

function clear(){
    pTitle.innerHTML = "";
    pDesp.innerHTML = "";
    pExplain.innerHTML = "";
    codeJava.innerHTML = "";
    codePython.innerHTML = "";
    textPython.style.display = "none";
    textJava.style.display = "none";
    codeJava.style.display = "none";
    codePython.style.display = "none";

}

function httpGet(url, callback) {
    // this function gets the contents of the URL. Once the
    // content is present it runs the callback function.
    var xmlhttp=new XMLHttpRequest();
    xmlhttp.onreadystatechange=function() {
        if (xmlhttp.readyState==4 && xmlhttp.status==200) {
            callback(xmlhttp.responseText);
        }
    }
    xmlhttp.open("GET", url, false);
    xmlhttp.send();    
}

var allProblems = document.querySelectorAll(".problem");
var problemDiv = document.querySelector("#sideProblem");
var pDesp = document.querySelector("#p-desp");
var pTitle = document.querySelector("#p-title");
var pExplain = document.querySelector("#p-explain");
var textPython = document.querySelector("#text-python");
var textJava = document.querySelector("#text-java");
var codePython = document.querySelector("#code-python");
var codeJava = document.querySelector("#code-java");
var aboutBtn = document.querySelector("#about");
var prevClick = aboutBtn;


allProblems.forEach(function(eachP){
    eachP.addEventListener("click", function(el){
        clear();
        problemDiv.style.display = "block";
        load(eachP.id);
        eachP.style.backgroundColor = "white";
        prevClick.style.backgroundColor = "#eee";
        prevClick = eachP;
    });
});

aboutBtn.addEventListener("click", function(){
    problemDiv.style.display = "none";
    aboutBtn.style.backgroundColor = "white";
    prevClick.style.backgroundColor = "#eee";
    prevClick = aboutBtn;
    
});