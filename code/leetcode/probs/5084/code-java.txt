class Solution {
    public TreeNode sufficientSubset(TreeNode root, int limit) {
        
        if (visit(root, 0, limit) < limit) return null;
        return root;
    } 
    
    public int visit(TreeNode root, int sum, int limit){
        
        // return max path sum starting this node, inclusive
        if (root == null) return 0;
        
        if (root.left == null && root.right == null){
            return root.val;
        }
        
        sum += root.val;
        int L = Integer.MIN_VALUE, R = Integer.MIN_VALUE;
        boolean left = true, right = true;
        
        if (root.left != null){
            L = visit(root.left, sum, limit);
            if (L + sum < limit) left = false;
        }
        if (root.right != null){
            R = visit(root.right, sum, limit);
            if (R + sum < limit) right = false;
        }
        if (left == false) root.left = null;
        if (right == false) root.right = null;
        
        return Math.max(L, R) + root.val;
    }
}