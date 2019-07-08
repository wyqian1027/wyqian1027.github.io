// using pointer
public class ZigzagIterator {
    
    int pointer = 0;
    int[] index;
    List<List<Integer>> input = new ArrayList<>();
    
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        index = new int[2];
        
        input.add(v1);
        input.add(v2);
    }

    public int next() {
        int val = 0;
        for (int i = pointer; i < pointer + 2; i++){
            int loc = i % 2;
            if (index[loc] < input.get(loc).size()){
                index[loc]++;
                val = input.get(loc).get(index[loc]-1);
                pointer = (i + 1) % 2;
                break;
            }
        }
        return val;
    }

    public boolean hasNext() {
        for (int i = pointer; i < pointer + 2; i++){
            int loc = i % 2;
            if (index[loc] < input.get(loc).size()){
                pointer = loc;
                return true;
            }
        }
        return false;
    }
}

// using iterator
public class ZigzagIterator {

    LinkedList<Iterator> list;
    public ZigzagIterator(List<Integer> v1, List<Integer> v2) {
        list = new LinkedList<>();
        if (!v1.isEmpty()) list.add(v1.iterator());
        if (!v2.isEmpty()) list.add(v2.iterator());
    }

    public int next() {
        Iterator iter = list.poll();
        int result = (Integer) iter.next();
        if (iter.hasNext()) list.offer(iter);
        return result;        
    }

    public boolean hasNext() {
        return !list.isEmpty();      
    }
}
