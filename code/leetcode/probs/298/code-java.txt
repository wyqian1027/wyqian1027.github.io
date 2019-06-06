class Solution {
    
    int longest = 0;
    
    public int longestConsecutive(TreeNode root) {
        if (root == null) return 0;
        dfs(root, root.val, 1);
        return longest;
    }

    private void dfs(TreeNode root, int val, int length) {
        
        if (root == null) return;

        longest = Math.max(longest, length);
        
        if (root.left != null){
            int L = (root.left.val == val + 1 ? 1+length : 1);
            dfs(root.left, root.left.val, L);
        }
        if (root.right != null){
            int R = (root.right.val == val + 1 ? 1+length : 1);
            dfs(root.right, root.right.val, R);
        }
    }
}