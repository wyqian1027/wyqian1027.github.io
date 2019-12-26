class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return check(root.left, root.right);
    }
    
    private boolean check(TreeNode n1, TreeNode n2){
        if (n1 == null && n2 == null) return true;
        if (n1 == null || n2 == null) return false;
        return n1.val == n2.val && check(n1.left, n2.right) && check(n1.right, n2.left);
    }
}