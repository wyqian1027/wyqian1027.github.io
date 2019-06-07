class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValid(root, Long.MIN_VALUE, Long.MAX_VALUE);  
    }
    
    private boolean isValid(TreeNode root, long lo, long hi){
        if (root == null) return true;
        if (lo < hi && lo < root.val && root.val < hi){
            return isValid(root.left, lo, root.val) && isValid(root.right, root.val, hi);
        }        
        return false;
    }
}

// Alternative BFS traversal or DFS inorder also works