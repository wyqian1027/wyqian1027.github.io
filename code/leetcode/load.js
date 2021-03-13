
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
    httpGet("probs/"+id+"/code-python.py", function(textFile){
        if (textFile != ""){
            textPython.style.display = "block";
            codePython.innerHTML = PR.prettyPrintOne(textFile, "python3");        
            codePython.style.display = "block";
        }
    });
    httpGet("probs/"+id+"/code-java.java", function(textFile){
        if (textFile != ""){
            textJava.style.display = "block";  
            // codeJava.innerHTML = PR.prettyPrintOne("", "java");
            codeJava.innerHTML = PR.prettyPrintOne(textFile.replace(/</g, "&lt;").replace(/>/g, "&gt;"), "java");
            codeJava.style.display = "block";
        }
    });
    httpGet("probs/"+id+"/code-cpp.cpp", function(textFile){
        if (textFile != ""){
            textCpp.style.display = "block";
            codeCpp.innerHTML = PR.prettyPrintOne(textFile, "cpp");   
            codeCpp.style.display = "block";
        }
    });
}

function clear(){
    pTitle.innerHTML = "";
    pDesp.innerHTML = "";
    pExplain.innerHTML = "";
    codeJava.innerHTML = "";
    codePython.innerHTML = "";
    codeCpp.innerHTML = "";
    textPython.style.display = "none";
    textJava.style.display = "none";
    textCpp.style.display = "none";
    codeJava.style.display = "none";
    codePython.style.display = "none";
    codeCpp.style.display = "none";
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

var htmlBody = document.querySelector("body")
var allProblems = document.querySelectorAll(".problem");
var problemDiv = document.querySelector("#sideProblem");
var pDesp = document.querySelector("#p-desp");
var pTitle = document.querySelector("#p-title");
var pExplain = document.querySelector("#p-explain");
var textPython = document.querySelector("#text-python");
var textJava = document.querySelector("#text-java");
var textCpp = document.querySelector('#text-cpp');
var codePython = document.querySelector("#code-python");
var codeJava = document.querySelector("#code-java");
var codeCpp = document.querySelector('#code-cpp');
var aboutBtn = document.querySelector("#about");
var darkBtn = document.querySelector("#dark");
var prevClick = aboutBtn;
var lastUpdate = new Date(document.lastModified);


allProblems.forEach(function(eachP){
    eachP.addEventListener("click", function(el){
        if (prevClick === eachP) return;
        clear();
        problemDiv.style.display = "block";
        load(eachP.id);
        eachP.style.backgroundColor = "#f5f9fa";
        eachP.style.fontWeight = "bold";
        prevClick.style.backgroundColor = "#eee";
        prevClick.style.fontWeight = "";
        prevClick = eachP;
    });
});

var numProblems = allProblems.length;
var tag1 = [["Bit Manipulation", "BIT"], ["Array", "ARRAY"], ["Binary Search", "BinarySearch"], ["Subarray", "SUBARRY"], ["Subsequence", "SUBSEQUENCE"], ["Subset", "SUBSET"], ["String", "STRING"], ["Mathematics", "MATH"], ["Stack", "STACK"],
            ["LinkedList","LINKEDLIST"], ["Priority Queue", "HEAP"], ["HashMap", "HASHMAP"], ["DP-1D", "DP-1D"], ["DP-2D", "DP-2D"], ["DP-Cache", "DP-CACHE"],
            ["Greedy", "GREEDY"],  ["Interval", "INTERVAL"], ["Binary Tree", "BT"], ["Binary Tree Traversal", "BTT"], ["N-ary Tree", "N-ary"], ["Trie", "TRIE"], ["BST", "BST"],
            ["Divide & Conquer", "D&C"], ["Backtracking", "BACKTRACKING"], ["BFS & DFS", "BFSDFS"], ["Sorting", "SORTING"], ["Graph", "GRAPH"], ["Union-Find", "UF"],
            ["Games", "GAME"], ["Design", "DESIGN"]];
var tag2 = [["# N Sum", "n-sum"], ["# Words", "words"], ["# Palindrome" , "palindrome"],
            ["# Parenthesis", "parenthesis"], ["# Sliding Window", "SW"], ["# Stock Problems", "stock"], ["# Robbery Problems", "robbery"], ["# Edit Distance","editDistance"], ["# Serialization", "serialization"],
            ["# Path", "path"], ["# Permutations", "permutations"], ["# Lowest Common Ancestor", "lca"], ["# Tree Convert", "tree-convert"],
            ["# Iterator", "iterator"], ["# Random", "RANDOM"], ["# Matrix/Board", "MATRIX"], ["# Topological Sorting", "TS"], ["# Bonus", "BONUS"]];
            
function setAbout(){
    aboutBtn.style.backgroundColor = "#f5f9fa";
    prevClick.style.backgroundColor = "#eee";
    prevClick.style.fontWeight = "";
    prevClick = aboutBtn;
    pTitle.style.display = "block";
    pTitle.innerHTML = "LeetCode Problem Solving Workbook ";
    pDesp.style.display = "block";
    pDesp.innerHTML = `<br>
    <p style="font-size: 22px">Total Number of Problems:  &nbsp; ${numProblems}<br> Last Update: &nbsp; ${lastUpdate.getFullYear() + "/" + (lastUpdate.getMonth()+1) + "/" + lastUpdate.getDate()}</p>
    <br>
    <p style="line-height: 1.5;">
    ${this.tag1.map((item, i) => 
        `<a class="tags" href="#${item[1]}"> ${item[0]}</a>
        `).join('&nbsp; ')}
    </p>
    <br>
    <p style="line-height: 1.5;">
    ${this.tag2.map((item, i) => 
        `<a class="tags" href="#${item[1]}"> ${item[0]}</a>
        `).join('&nbsp; ')}
    </p>

    <br>
    <br>
    <br>
    <br>
    <p>Read me:<br>
    <br>
    1. This workbook attempts to categorize some popular LeetCode problems. Explanations are kept to minimum intentionally.<br>
    <br>
    2. The website is static. Each problem sends an XMLHttpRequest to the Database for the related textfile so as to render the description and solutions<br>
    <br>
    3. Some Java solutions may have missing "<" or ">" or content inside, due to a problem with prettify engine used to render the codes.<br>
    <br>
    4. #BONUS tag is problems I found outside LeetCode. <br>
    <br><br> June, 2019</p>
    <br>
    <a style="position: absolute; down: 0" title="Go Back" href="https://wyqian1027.github.io/public/coding.html"><i class="fas fa-igloo"></i> Go Back To HomePage</a><br>`;    
}

aboutBtn.addEventListener("click", function(){
    // problemDiv.style.display = "none";
    if (prevClick === aboutBtn) return;
    clear();
    setAbout();
});


// var darkStatus = false
// darkBtn.addEventListener("click", function(){
//     if (darkStatus === false){
//         htmlBody.backgroundColor = "black";
//         htmlBody.color = "white";
//     } else {
//         htmlBody.backgroundColor = "white";
//         htmlBody.color = "black";
//     }
    
//     darkStatus ^= true;
// })

window.onload = function(){
    setAbout();
}