class Vertex {

    constructor(id, key=Infinity){
        this.id = id;
        this.key = key;
        this.neighborID = [];
        this.neighborWT = [];
    }

    // add new neighbors
    addNei(neiID, neiWT=0) {
        if (!this.hasNei(neiID)){
            this.neighborID.push(neiID);
            this.neighborWT.push(neiWT);
        } 
    }

    // check if neighbor already exists
    hasNei(neiID=-1){
        if (neiID == -1) return this.neighborID.length > 0;
        return this.neighborID.includes(neiID);
    }

    getNeis(){
        return this.neighborID;
    }

    getNeiWTs(){
        return this.neighborWT;
    }

    getNeiWT(neiID){
        if (!this.hasNei(neiID)) return -1;
        return this.neighborWT[this.neighborID.indexOf(neiID)];
    }
}

// undirected graph
class Graph {

    constructor() {
        this.numV = 0;
        this.numE = 0;
        this.adj = new Map();

    }

    // add vertex
    addVertex(id){
        if (this.adj.has(id)) return this.adj.get(id);
        this.numV += 1;
        this.adj.set(id, new Vertex(id));
        return this.adj.get(id);
    }

    // add undirectional weight edge
    addEdge(id1, id2, wt=0){
        this.addVertex(id1);
        this.addVertex(id2);
        var v1 = this.getV(id1);
        var v2 = this.getV(id2);
        if (!v1.hasNei(id2)){
            v1.addNei(id2, wt);
            this.numE += 1;
        }
        if (!v2.hasNei(id1)){
            v2.addNei(id1, wt);
        }
    }

    relaxNeiKey(id1, id2){
        var v1 = this.getV(id1);
        if (!v1.hasNei(id2)) return -1;
        var v2 = this.getV(id2);
        v2.key = Math.min(v2.key, v1.key + v1.getNeiWT(id2));
        return v2.key;
    }

    hasV(id){
        return this.adj.has(id);
    }

    getV(id){
        if (this.hasV(id)){
            return this.adj.get(id);
        }
        return null;        
    }

    clear(){
        this.numV = 0;
        this.adj = new Map();
    }
}


