class Queue {
    constructor(items = []){
        this.items = items;
    }

    enqueue(element){
        this.items.push(element);
    }

    dequeue(){
        if (this.isEmpty()) return null;
        return this.items.shift();
    }

    peek(){
        if (this.isEmpty()) return null;
        return this.items[0];
    }

    isEmpty() {
        return this.items.length == 0;
    }

    print(){
        var str = ""; 
        for(var i = 0; i < this.items.length; i++) str += this.items[i] +" "; 
        return str;
    }
}

class PQElement {
    constructor(id, key, prevID=-1){
        this.id = id;
        this.key = key;
        this.prevID = prevID
    }

}


// https://truetocode.com/binary-treemax-heap-priority-queue-and-implementation-using-javascript/427/
class PQueue {
    constructor(array) {
      this.array = [null, ...array]; 
      this.size = array.length
    }

    arrange(idx) {
      while (idx > 1 && this.compare(Math.floor(idx / 2), idx)) {
        this.swap(idx, Math.floor(idx / 2));
        idx = Math.floor(idx / 2);
      }
    }
   
    heaper(idx1) {
      while (2 * idx1 <= this.size) {
        let idx2 = 2 * idx1;
        if (idx2 < this.size && this.compare(idx2, idx2 + 1)) idx2++;
        if (!this.compare(idx1, idx2)) break;
        this.swap(idx1, idx2);
        idx1 = idx2;
      }
    }
   
    rootdelete() {
      let min = this.array[1]
      this.swap(1, this.size--);
      this.heaper(1);
      this.array[this.size + 1] = null;
      return min;
    }
   
    insert(element) {
      this.array[++this.size] = element;
      this.arrange(this.size);
    }
   
    compare(idx1, idx2) {
      return this.array[idx1].key > this.array[idx2].key;
    }
   
    swap(idx1, idx2) {
      const temp = this.array[idx1];
      this.array[idx1] = this.array[idx2];
      this.array[idx2] = temp;
    }

    returnall(){
      return this.array;
    }

  }