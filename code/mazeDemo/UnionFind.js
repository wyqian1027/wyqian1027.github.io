class UnionFind {
    constructor(size){
        this.p = new Map();
        this.rank = new Map();
        this.size = size;
        this.addSets(size);
    }

    makeset(item){
        this.p.set(item, item);
        this.rank.set(item, 0);
    }

    addSets(items){
        for (var x = 0; x < this.size; x++){
            this.addSet(x);
        }
    }

    addSet(item){
        this.makeset(item);
    }

    find(x){
        if (this.p.get(x) != x){
            this.p.set(x, this.find(this.p.get(x)));
        }
        return this.p.get(x);
    }

    union(x, y){
        var xr = this.find(x);
        var yr = this.find(y);

        if (xr == yr) return false;
        if (this.rank.get(xr) < this.rank.get(yr)) {
            var tmp = xr;
            xr = yr;
            yr = tmp;
        }
        // console.log(xr, yr)
        this.p.set(yr, xr);
        if (this.rank.get(xr) == this.rank.get(yr)) {
            this.rank.set(xr, this.rank.get(xr) + 1);
        }
        return true;
    }
}