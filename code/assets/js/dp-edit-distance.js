function getEditDist(word1, word2, flag=true) {
    
    var l1 = word1.length, l2 = word2.length;

    // Initialization dp matrix
    var dp = [];
    dp[0] = [];
    dp[0][0] = 0;
    
    // Base cases, word2 on the rows
    for (var i=1; i<l2+1; i++){
        dp[i] = [];
        dp[i][0] = i;
    }
    for (var i=1; i<l1+1; i++){
        dp[0][i] = i;
    }
    
    //Recursion steps:
    for (var i=1; i<l2+1; i++){
        for (var j=1; j<l1+1; j++){
            if (word2[i-1] === word1[j-1]){
                dp[i][j] = Math.min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]);
            } else {
                dp[i][j] = Math.min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1);
            }
        }
    }
    if (flag === true ){
        return [dp[l2][l1], dp];
    } else {
        return dp[l2][l1];
    }
    
};

// <table>
//   <tr>
//     <td>Jill</td>
//     <td>Smith</td>
//     <td>50</td>
//   </tr>
//   <tr>
//     <td>Eve</td>
//     <td>Jackson</td>
//     <td>94</td>
//   </tr>
//   <tr>
//     <td>John</td>
//     <td>Doe</td>
//     <td>80</td>
//   </tr>
// </table>


function makeBoard(word1, word2){
    var res = getEditDist(word1, word2);
    var minDist = res[0];
    var matrix = res[1];
    var l1 = word1.length, l2 = word2.length;
    var out = `<table style="font-size:20px" align="center">`;
    
    out+= "<tr>"
    for (var i=-1; i<l1+1; i++){
        out += `<td style="padding: 5px 12px; font-size: 20px; color: #FF6E69; font-weight: bold">${ i>=1 ? word1[i-1] : ""}</td>`
    }
    out+= "</tr>"
    for (var i=0; i<l2+1; i++){
        out += "<tr>";
        out += `<td style="padding: 5px 12px; font-size: 20px; color: #7F7AFF; font-weight: bold">${ i!=0 ? word2[i-1] : ""}</td>`
        for (var j=0; j<l1+1; j++){
            if (i== l2 && j == l1){
                out += `<td style="padding: 5px 12px; font-size: 20px; background-color: red; color: white">${matrix[i][j]}</td>`
            } else {
                out += `<td style="padding: 5px 12px; font-size: 20px">${matrix[i][j]}</td>`
            }
            
        }
        out += "</tr>";
    }
    return out;
}




const w1 = document.querySelector("#word1");
const w2 = document.querySelector("#word2");
const msg = document.querySelector("#message");
const board = document.querySelector("#board");
const inputSentence = document.querySelector("#input-sentence");
const outputSentence = document.querySelector("#output-sentence");
const checkBtn = document.querySelector('#check-btn');
var myDict;

w1.addEventListener("input", function (e) {
    msg.innerHTML = `Edit Distance = ${getEditDist(w2.value, w1.value)[0]}`;
    board.innerHTML = makeBoard(w2.value, w1.value);
});

w2.addEventListener("input", function (e) {
    msg.innerHTML = `Edit Distance = ${getEditDist(w2.value, w1.value)[0]}`;
    board.innerHTML = makeBoard(w2.value, w1.value);

});

msg.innerHTML = `Edit Distance = ${getEditDist(w2.value, w1.value)[0]}`;
board.innerHTML = makeBoard(w2.value, w1.value);    



// plan to do! 
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

httpGet("assets/file/10kcommon.txt", function(textFile){
    myDict = textFile.slice(1, -1).split("\n");
    // console.log(myDict);
});



function findNearest(word, myDict){
    if (word === "") return "";
    if (word === " ") return " ";
    var minDist = 100;
    var minWord = 0;
    for (var i=0; i<myDict.length; i++){
        if (myDict[i] === word) return word;
        var d = getEditDist(word, myDict[i], false);
        if (d < minDist){
            minDist = d;
            minWord = i;
        }
    }
    return myDict[minWord];
}

function getCorrectedSentence(myDict){
    var input = inputSentence.value.split(/\W+/);
    // console.log(input)
    var output = "";
    for (var i=0; i<input.length; i++){
        output += findNearest(input[i], myDict) + " ";
    }
    return output;
}


checkBtn.addEventListener("click", function(e){
    var corrected = getCorrectedSentence(myDict);
    outputSentence.innerHTML = getCorrectedSentence(myDict);
}) 








