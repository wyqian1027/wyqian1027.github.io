// GLOBAL PARAMETERS
// var CANVAS_WIDTH = 600;
// var CANVAS_HEIGHT = 600;
var HSPACE = 25;
var VSPACE = 25;

var START_LOCATION_COLOR = "red";
var END_LOCATION_COLOR = "blue";
var BACKGROUND_COLOR = "black";
var EDGE_COLOR = "white";

var MAX_STEPS = 10000;
var EDGE_WIDTH = 4;
var POINT_SIZE = 1;
var BOUNDARY = 40;
var POINTSIZE = 8;
var DIRECTIONS = [[-HSPACE, 0], [HSPACE, 0], [0, VSPACE], [0, -VSPACE]];

var mazeBtns = document.querySelectorAll(".maze-types");
var settingBtns = document.querySelectorAll(".options");
var infoSpan = document.querySelector(".info");

// var canvas = document.getElementById('canvas');
// canvas.width = CANVAS_WIDTH;
// canvas.height = CANVAS_HEIGHT;
// var ctx = canvas.getContext('2d');
var endID = -1;
var graph = new Graph();
var grid = new Grid(CANVAS_WIDTH, CANVAS_HEIGHT, BOUNDARY, HSPACE, VSPACE)
var visited = Array(grid.numPoints).fill(0);
var steps = MAX_STEPS;
var path = [];
var currentMaze = "";

grid.buildGrid();

var buildRandomCompleteGraph = function(maxRN = 100){
    var dummyG = new Graph();
    for (var id = 0; id < grid.numPoints; id++){
        var neiIDs = grid.getNeiIDs(id);
        for (var i = 0; i < neiIDs.length; i++){
            var neiID = neiIDs[i];
            var rndW = Math.floor(Math.random()*maxRN);
            dummyG.addEdge(id, neiID, rndW);
        }
    }
    return dummyG;
}

//================ 1. DFS MAZE ==================

var make_DFS_Maze = function() {

    clearCanvas();
    fillCanvasBackground();
    graph.clear();
    visited = Array(grid.numPoints).fill(0);
    steps = MAX_STEPS;
    path = []

    graph.addVertex(0);
    DFS_helper(0);

    var startCoor = grid.getCenterCoor();
    var startID = grid.getCenterID();
    drawPoint(startCoor[0], startCoor[1], START_LOCATION_COLOR, POINTSIZE);
    var endCoor = grid.getCoorfromID(endID);
    drawPoint(endCoor[0], endCoor[1], END_LOCATION_COLOR, POINTSIZE);
    path = findPathBFS(startID, endID);
        
};

var DFS_helper = function(id1){
  
    if (steps-- <= 0) return;
    visited[id1] = 1;
    var v1 = graph.getV(id1);
    endID = id1;

    var p = [0, 1, 2, 3]; 
    permutate(p);
    var [x1, y1] = grid.getCoorfromID(id1);

    for (var i = 0; i < 4; i++){
        var x2 = x1 + DIRECTIONS[p[i]][0];
        var y2 = y1 + DIRECTIONS[p[i]][1];

        if (grid.isValidCoor(x2, y2)) {
            var id2 = grid.getIDfromCoor(x2, y2);
            if (visited[id2] == 0) {
                drawEdge(x1, y1, x2, y2, EDGE_COLOR, EDGE_WIDTH);
                graph.addEdge(id1, id2);
                DFS_helper(id2);            
            }
        } 
    }
    visited[id1] = 2;
};

//================ 2. Kruskal MAZE ==================
var make_Kruskal_Maze = function(){
    clearCanvas();
    fillCanvasBackground();
    graph.clear();
    steps = MAX_STEPS;
    path = [];

    maxRN = 1000;
    var dummyG = buildRandomCompleteGraph(maxRN); 
    var pq = new PQueue([])
    var seenEdges = new Set();
    for (var id = 0; id < grid.numPoints; id++){
        var neiIDs = dummyG.getV(id).getNeis();
        var neiWTs = dummyG.getV(id).getNeiWTs();
        for (var i = 0; i < neiIDs.length; i++){
            var neiWT = neiWTs[i];
            var neiID = neiIDs[i];
            if (!seenEdges.has(id+"-"+neiID) && !seenEdges.has(neiID+"-"+id)){
                pq.insert(new PQElement(id, neiWT, neiID));
                seenEdges.add(id+"-"+neiID);
            }
        }
    }
    var uf = new UnionFind(grid.numPoints);
    var visited = new Set();
    while (pq.size != 0){
        if (steps-- <= 0) break;
        var cur = pq.rootdelete();
        var u = cur.id;
        var v = cur.prevID;
        if (uf.find(u) != uf.find(v)){
            uf.union(u, v);
            graph.addEdge(u, v);
            var [x1, y1] = grid.getCoorfromID(u);
            var [x2, y2] = grid.getCoorfromID(v);
            drawEdge(x1, y1, x2, y2, EDGE_COLOR, EDGE_WIDTH);
            visited.add(u);
            visited.add(v);
        }
    }

    var startCoor = grid.getCenterCoor();
    var startID = grid.getCenterID();
    drawPoint(startCoor[0], startCoor[1], START_LOCATION_COLOR, POINTSIZE);

    while (true){
        endID = grid.getRandomID();
        if (visited.has(endID)) break;
    }
    var endCoor = grid.getCoorfromID(endID);

    drawPoint(endCoor[0], endCoor[1], END_LOCATION_COLOR, POINTSIZE);
    path = findPathBFS(startID, endID);
}

//================ 3. Prim MAZE ==================

var make_Prim_Maze = function(){
    clearCanvas();
    fillCanvasBackground();
    graph.clear();
    steps = MAX_STEPS;
    path = [];
    
    maxRN = 1000;
    // var dummyG = buildRandomCompleteGraph(maxRN); // precompute random weights is not necessary
    var root = grid.getRandomID()
    var pq = new PQueue([new PQElement(root, 0, root)])
    var visited = new Set();
    var keys = Array(grid.numPoints).fill(Infinity);
    keys[root] = 0;

    while (visited.size != grid.numPoints){
        var u = pq.rootdelete(); // u.id, u.key, u.prevID
        if (steps-- <= 0) break;
        if (u == null) break;
        var curID = u.id;
        var curKey = u.key;
        var prevID = u.prevID;

        if (visited.has(curID)) continue;

        var [x1, y1] = grid.getCoorfromID(prevID);
        var [x2, y2] = grid.getCoorfromID(curID);
        var neiIDs = grid.getNeiIDs(curID);

        visited.add(curID);
        drawEdge(x1, y1, x2, y2, EDGE_COLOR, EDGE_WIDTH);
        graph.addEdge(curID, prevID);

        for (var i = 0; i < neiIDs.length; i++){
            var neiID = neiIDs[i];
            var rndW = Math.floor(Math.random()*maxRN);
            // var rndW = dummyG.getV(curID).getNeiWT(neiID);
            if (keys[neiID] > curKey + rndW) {
                keys[neiID] = curKey + rndW;
                pq.insert(new PQElement(neiID, keys[neiID], curID))
            }
        }
    }

    var startCoor = grid.getCenterCoor();
    var startID = grid.getCenterID();
    drawPoint(startCoor[0], startCoor[1], START_LOCATION_COLOR, POINTSIZE);
    while (true){
        endID = grid.getRandomID();
        if (visited.has(endID)) break;
    }
    var endCoor = grid.getCoorfromID(endID);

    drawPoint(endCoor[0], endCoor[1], END_LOCATION_COLOR, POINTSIZE);
    path = findPathBFS(startID, endID);

}

//================ SOLUTION: Path Finding ==================
var findPathBFS = function(startID, endID){

    var queue = new Queue([startID]);
    var routes = new Queue([[startID]]);
    var seen = new Set();
    seen.add(startID);

    while (!queue.isEmpty()) {
        var curID = queue.dequeue();
        var curRoute = routes.dequeue();
        var vertex = graph.getV(curID);
        if (vertex != null && vertex.hasNei()){
            var neiIDs = vertex.getNeis();
            for (var i = 0; i < neiIDs.length; i++){
                var neiID = neiIDs[i];
                if (!seen.has(neiID)){
                    var newRoute = curRoute.slice();
                    newRoute.push(neiID);
                    if (neiID == endID) return newRoute;
                    queue.enqueue(neiID);
                    routes.enqueue(newRoute);
                    seen.add(neiID);
                }
            }
        }
    }
    return [] ;
};


// Event Listeners
var makeMazeByType = function(mazeType){
    currentMaze = mazeType;
    setInfoStatus("none");
    if (mazeType=="DFS"){
        make_DFS_Maze();
    } else if (mazeType=="KRUSKAL"){
        make_Kruskal_Maze();
    } else if (mazeType=="PRIM"){
        make_Prim_Maze();
    }
};

var changeSettings = function(settingType){
    if (settingType =="Show Path"){
        displaySolution(path);
        writeToInfo(grid.numPoints, MAX_STEPS, currentMaze, path.length);
    } else if (settingType == "Set Maze Depth"){
        MAX_STEPS = parseInt(prompt("Please sets Maximum Maze Depth: ", "2000"));
        make_DFS_Maze();
        setInfoStatus("none");
    }
};

settingBtns.forEach(function(el, i){
    el.addEventListener("click", function(){
        changeSettings(el.innerHTML);
    });
});

mazeBtns.forEach(function(el, i){
    el.addEventListener("click", function(){
        makeMazeByType(el.innerHTML);
    });
});

var setInfoStatus = function(status){
    infoSpan.style.display = status
};

var writeToInfo = function(numV, maxDepth, mazeType, pathLength){
    infoSpan.innerHTML = "Maze: " + mazeType + "&nbsp;  total vertices: " + numV + "&nbsp;  max depth: " + maxDepth + "&nbsp; path length: " +pathLength;
    setInfoStatus("block");
}

// main
var init = function(){
    make_DFS_Maze();
}

init();