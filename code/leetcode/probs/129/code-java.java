class Solution {
    
    int res = 0;
    
    public int sumNumbers(TreeNode root) {
        dfs(root, 0);
        return res;
    }
    
    private void dfs(TreeNode root, int num) {
        if (root == null) return;
        
        if (root.left == null && root.right == null){
            res += (num*10 + root.val);
            return;
        }
        
        if (root.left != null) dfs(root.left, num*10 + root.val);
        if (root.right != null) dfs(root.right, num*10 + root.val);
    }
}