class Solution {
    
    int res = 0;
    
    public int countUnivalSubtrees(TreeNode root) {
        
        check(root);
        return res;
    }
    
    private boolean check(TreeNode root) {
        
        if (root == null) return false;
        
        if (root.left == null && root.right == null) {
            res += 1;
            return true; 
        }
        
        boolean L = true, R = true;
        
        if (root.left != null) {
            L = check(root.left);
            L = L && (root.left.val == root.val);
        }
        
        if (root.right != null) {
            R = check(root.right);
            R = R && (root.right.val == root.val);
        }
        
        if (L && R == true) res += 1;
        
        return (L && R);       
    }
}