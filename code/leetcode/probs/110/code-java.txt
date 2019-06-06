// 1. O(N^2) worst case:

class Solution {
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        if (root.left == null && root.right == null) return true;
        return isBalanced(root.left) && isBalanced(root.right) && Math.abs(getDepth(root.left)-getDepth(root.right)) <= 1;
    }
    
    
    private int getDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(getDepth(root.left), getDepth(root.right));
    }
}


// 2. O(N) improved solution with global flag:

class Solution {

    boolean res = true;
    
    public boolean isBalanced(TreeNode root) {
        getDepth(root);
        return res;
    }
    
    private int getDepth(TreeNode root) {
        if (root == null) return 0;
        int L = getDepth(root.left);
        int R = getDepth(root.right);
        if (Math.abs(L - R) > 1) res = false;
        return 1 + Math.max(L, R);    
    }
}