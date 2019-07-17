// Grid defines where our Graph sets in
class Grid {
    constructor(width, height, boundary, hspace, vspace){
        this.w = width;
        this.h = height;
        this.pad = boundary;
        this.hs = hspace;
        this.vs = vspace;
        this.mapCoor2ID = new Map();
        this.mapID2Coor = new Map();
        this.numPoints = 0;

    }

    isValidCoor(x, y){
        return this.mapCoor2ID.has(x+"-"+y);
    }

    isValidID(id){
        return 0 <= id && id <= this.numPoints;
    }

    findTopLeft(){
        var [curX, curY] = this.getCenterCoor();
        while (curX - this.hs >= this.pad) curX -= this.hs;
        while (curY - this.vs >= this.pad) curY -= this.vs;
        return [curX, curY];
    }

    buildGrid(){
        var [startX, startY] = this.findTopLeft();
        var id = 0;
        for (var x = startX; x <= this.w - this.pad; x += this.hs){
            for (var y = startY; y <= this.h - this.pad; y += this.vs){
                this.mapCoor2ID.set(x+"-"+y, id);
                this.mapID2Coor.set(id, x+"-"+y);
                id += 1;
            }
        }
        this.numPoints = id;
        return true;
    }

    getCenterCoor(){
        return [Math.floor(this.w / 2), Math.floor(this.h / 2)];
    }
    getCenterID(){
        return this.mapCoor2ID.get(this.getCenterCoor().join("-"));
    }

    getRandomID(){
        return Math.floor(Math.random()*this.numPoints);
    }

    getRandomCoor(){
        return this.getCoorfromID(this.getRandomID());
    }

    getIDfromCoor(x, y){
        return this.mapCoor2ID.get(x+"-"+y);
    }

    getCoorfromID(id){

        var coor = this.mapID2Coor.get(id).split("-");
        return [parseInt(coor[0]), parseInt(coor[1])];
    }

    getNeiIDs(id){
        var neis = [];
        var [x, y] = this.getCoorfromID(id);
        if (this.isValidCoor(x - this.hs, y)) neis.push(this.getIDfromCoor(x - this.hs, y));
        if (this.isValidCoor(x + this.hs, y)) neis.push(this.getIDfromCoor(x + this.hs, y));
        if (this.isValidCoor(x, y - this.vs)) neis.push(this.getIDfromCoor(x, y - this.vs));
        if (this.isValidCoor(x, y + this.vs)) neis.push(this.getIDfromCoor(x, y + this.vs));
        return neis;
    }
}


// small testcases
// var g = new Grid(300, 400, 50, 41, 28)
// g.buildGrid();
// for(var i = 0; i < 300; i++) drawPoint(g.getRandomCoor()[0], g.getRandomCoor()[1], "blue", 10);
// var randomID = g.getRandomID();
// drawPoint(g.getCoorfromID(randomID)[0], g.getCoorfromID(randomID)[1], "green", 10);
// for(var i = 0; i < g.getNeiIDs(randomID).length; i++){
//     var neiID = g.getNeiIDs(randomID)[i];
//     drawPoint(g.getCoorfromID(neiID)[0], g.getCoorfromID(neiID)[1], "red", 10);
// }