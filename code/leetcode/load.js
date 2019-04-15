function load(element, url) {
    var file = new XMLHttpRequest();
    file.open("GET", url, true);
    file.onreadystatechange = function() {
      if (file.readyState === 4) {  // Makes sure the document is ready to parse
        if (file.status === 200) {  // Makes sure it's found the file
          var text = file.responseText;
          element.innerHTML = text;
        }
      }
    }
}

var allProblems = document.querySelectorAll(".problem");
var problemDesp = document.querySelector("#p-desp");

allProblems.forEach(function(eachP){
    eachP.addEventListener("click", function(el){
        var url = "https://wyqian1027.github.io/public/code/leetcode/probs/"+eachP.id+"/description.txt";
        console.log(url);
        load(problemDesp, url)
    });
});