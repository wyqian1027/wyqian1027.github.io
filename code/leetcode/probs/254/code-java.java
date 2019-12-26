// 1. Naive implementation (100ms)

class Solution {
    
    public List<List<Integer>> getFactors(int n) {
        List<List<Integer>> res = new ArrayList<>();
        dfs(2, n, new ArrayList<Integer>(), res);
        res.remove(res.size()-1);
        return res;
    }
    
    private void dfs(int start, int n, List<Integer> path, List<List<Integer>> res) {
        
        if (n == 1) {
            res.add(new ArrayList<Integer>(path));
            return;
        }
        
        for (int i = start; i <= n; i++){
            if (n % i == 0){
                path.add(i);
                dfs(i, n / i, path, res);
                path.remove(path.size() - 1);
            }
        }
    }
}

// 2. Improvement on For Loop stop at sqrt(n)   (1ms!!!)

class Solution {
    
    public List<List<Integer>> getFactors(int n) {
        
        List<List<Integer>> res = new ArrayList<>();
        dfs(2, n, new ArrayList<Integer>(), res);
        return res;
    }
    
    private void dfs(int start, int n, List<Integer> path, List<List<Integer>> res) {
        
        if (n == 1) {
            if (path.size() > 1) {
                res.add(new ArrayList<Integer>(path)); 
            }
            return;
        }
        
        for (int i = start; i <= Math.sqrt(n); i++){  // using sqrt to get much better performance!!
            if (n % i == 0){
                path.add(i);
                dfs(i, n / i, path, res);
                path.remove(path.size() - 1);
            }
        }
        // added corner case
        int i = n;
        path.add(i);
        dfs(i, n / i, path, res);
        path.remove(path.size() - 1);
    }
}

