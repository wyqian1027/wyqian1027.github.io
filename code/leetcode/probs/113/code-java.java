//Backtracking Solution:

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        dfs(root, sum, new ArrayList<Integer>(), res);
        return res;
    }
    
    private void dfs(TreeNode root, int sum, List<Integer> path, List<List<Integer>> res) {
        
        if (root == null) return;
        
        sum -= root.val;
        path.add(root.val);
        if (root.left == null && root.right == null && sum == 0) {
            res.add(new ArrayList<>(path));
        } 
        
        if (root.left != null) {
            dfs(root.left, sum, path, res);
        }
        if (root.right != null) {
            dfs(root.right, sum, path, res);
        }
        path.remove(path.size()-1);
    }
}