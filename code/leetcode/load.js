
function load(id) {
    httpGet("probs/"+id+"/description.txt", function(textFile){
        var raw = textFile.split('\n').slice(1).join("<br>");
        raw = raw.replace(/Input/g, "<strong>Input</strong>");
        raw = raw.replace(/Output/g, "<strong>Output</strong>");
        pDesp.innerHTML = raw;
        pTitle.innerHTML = textFile.split('\n')[0];
    });
    httpGet("probs/"+id+"/explanation.txt", function(textFile){
        if (textFile != ""){
            pExplain.innerHTML = textFile.split('\n').join("<br>");;        
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
        if (prevClick === eachP) return;
        clear();
        problemDiv.style.display = "block";
        load(eachP.id);
        eachP.style.backgroundColor = "#f5f9fa";
        prevClick.style.backgroundColor = "#eee";
        prevClick = eachP;
    });
});

var numProblems = allProblems.length;

function setAbout(){
    aboutBtn.style.backgroundColor = "#f5f9fa";
    prevClick.style.backgroundColor = "#eee";
    prevClick = aboutBtn;
    pTitle.style.display = "block";
    pTitle.innerHTML = "LeetCode Problem Solving Workbook";
    pDesp.style.display = "block";
    pDesp.innerHTML = `
    Total Number of Problems: ${numProblems}<p>Please let me know if there is any mistake or typo. Thank you!<p>
    <a title="Go Back" href="https://wyqian1027.github.io/public/coding.html">Go Back <i class="fas fa-igloo"></i></a>`;    
}

aboutBtn.addEventListener("click", function(){
    // problemDiv.style.display = "none";
    if (prevClick === aboutBtn) return;
    clear();
    setAbout();
});

window.onload = function(){
    setAbout();
}