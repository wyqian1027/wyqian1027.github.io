class Solution {
    public List<List<Integer>> combinationSum3(int k, int n) {
        
        List<List<Integer>> res = new ArrayList<>();
        dfs(k, n, 1, new ArrayList<Integer>(), res);
        return res;
    }
    
    private void dfs(int k, int n, int start, List<Integer> path, List<List<Integer>> res) {
        
        if (k == 0 && n == 0){
            res.add(new ArrayList<Integer>(path));
            return;
        } else if (k == 0) {
            return;
        }
        
        for (int i = start; i <= 9; i++){
            
            if (n - i >= 0) {
                path.add(i);
                dfs(k-1, n - i, i+1, path, res);
                path.remove(path.size() - 1);
            }  
        }
    }
}