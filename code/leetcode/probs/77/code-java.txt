class Solution {
    public List<List<Integer>> combine(int n, int k) {
        
        List<List<Integer>> res = new ArrayList<>();
        dfs(1, n, k, new ArrayList<Integer>(), res);
        
        return res;
    }
    
    private void dfs(int start, int end, int k, List<Integer> path, List<List<Integer>> res){
        
        if (k == 0){
            res.add(new ArrayList<Integer>(path));
            return;
        }
        
        for (int i = start; i <= end+1-k; i++){ // get rid of insufficient choices...
            path.add(i);
            dfs(i+1, end, k-1, path, res);
            path.remove(path.size() - 1);
            
        }
    }
}