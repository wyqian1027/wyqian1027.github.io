
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

var htmlBody = document.querySelector("body")
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
var darkBtn = document.querySelector("#dark");
var prevClick = aboutBtn;


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
            ["LinkedList","LINKEDLIST"], ["Heap", "HEAP"], ["HashMap", "HASHMAP"], ["DP-1D", "DP-1D"], ["DP-2D", "DP-2D"], ["DP-Cache", "DP-CACHE"],
            ["GREEDY", "GREEDY"], ["Binary Tree", "BT"], ["Binary Tree Traversal", "BTT"], ["N-ary Tree", "N-ary"], ["Trie", "TRIE"], ["BST", "BST"],
            ["Divide & Conquer", "D&C"], ["Backtracking", "BACKTRACKING"], ["BFS & DFS", "BFSDFS"], ["Sorting", "SORTING"], ["Graph", "GRAPH"], ["Union-Find", "UF"],
            ["Games", "GAME"], ["Design", "DESIGN"]];
var tag2 = [["# N Sum", "n-sum"], ["# Words", "words"], ["# Prefix", "prefix"], ["# Palindrome" , "palindrome"],
            ["# Parenthesis", "parenthesis"], ["# Stock Problems", "stock"], ["# Robbery Problems", "robbery"], ["# Edit Distance","editDistance"], ["# Serialization", "serialization"],
            ["# Path", "path"], ["# Permutations", "permutations"], ["# Lowest Common Ancestor", "lca"], ["# Tree Convert", "tree-convert"],
            ["# Iterator", "iterator"], ["# Random", "RANDOM"], ["# Topological Sorting", "TS"]];
            
function setAbout(){
    aboutBtn.style.backgroundColor = "#f5f9fa";
    prevClick.style.backgroundColor = "#eee";
    prevClick.style.fontWeight = "";
    prevClick = aboutBtn;
    pTitle.style.display = "block";
    pTitle.innerHTML = "LeetCode Problem Solving Workbook";
    pDesp.style.display = "block";
    pDesp.innerHTML = `<br>
    <p style="font-size: 22px">Total Number of Problems: ${numProblems}</p>
    <br><p style="line-height: 1.5;">
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