// 1. Using Cache

class Solution {
    
    public int depthSumInverse(List<NestedInteger> nestedList) {
    
        List<List<Integer>> res = new ArrayList<>();
        getSum(nestedList, 1, res);
        int depth = res.size();
        int ans = 0;
        for (List<Integer> list: res){
            int s = 0;
            for (Integer x: list){
                s += x;
            }
            ans += s*depth;
            depth--;
        }
        return ans;
    }

    private void getSum(List<NestedInteger> nestedList, int level, List<List<Integer>> res){
        
        if (res.size() < level) {
            res.add(new ArrayList<>());
        }
        for (NestedInteger x: nestedList){
            if (x.isInteger()){
                res.get(level - 1).add(x.getInteger());
            } else {
                getSum(x.getList(), level + 1, res);
            }
        }
    }
}

// 2. BFS with layer sum
class Solution {
    public int depthSumInverse(List<NestedInteger> nestedList) {
    
        Queue<NestedInteger> q = new LinkedList<NestedInteger>();
        
        for (NestedInteger x: nestedList) q.offer(x);
        int res = 0;
        int prev = 0;
        
        while(!q.isEmpty()){
            
            int size = q.size();
            int levelSum = 0;
            for (int i = 0; i < size; i++){
                NestedInteger cur = q.poll();
                if (cur.isInteger()){
                    levelSum += cur.getInteger();
                } else {
                    for (NestedInteger nxt: cur.getList()){
                        q.offer(nxt);
                    }
                }
            }
            prev += levelSum;
            res += prev;
            
        }
        return res;
    }
}