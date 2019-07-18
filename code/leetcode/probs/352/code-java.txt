// Nice usage of Java's TreeMap
// O(lgN) for addNum 
// O(N) for getIntervals

class SummaryRanges {

    /** Initialize your data structure here. */
    TreeMap<Integer, int[]> root;
        
    public SummaryRanges() {
        
        root = new TreeMap<>();
    }
    
    public void addNum(int val) {
        if (root.containsKey(val)) return;
        Integer l = root.lowerKey(val);
        Integer h = root.higherKey(val);
        if (l != null && h != null && root.get(l)[1] + 1 == val && h - 1 == val){
            root.get(l)[1] = root.get(h)[1];
            root.remove(h);
        } else if (l != null && root.get(l)[1] + 1 >= val) {
            root.get(l)[1] = Math.max(val, root.get(l)[1]);
        } else if (h != null && root.get(h)[0] - 1 == val){
            root.put(val, new int[]{val, root.get(h)[1]});
            root.remove(h);
        } else {
            root.put(val, new int[]{val, val});
        }
    }
    
    public int[][] getIntervals() {
        
        int[][] res = new int[root.size()][2];
        int i = 0;
        for (int[] pair: root.values()) {
            res[i++] = pair;
        }
        return res;
    }
}