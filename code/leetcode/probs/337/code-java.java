class Solution {
        
    public int rob(TreeNode root) {
        int[] res = calculate(root);
        return Math.max(res[0], res[1]);
    }
    
    private int[] calculate(TreeNode root){
        if (root == null) return new int[2];
        
        int[] left = calculate(root.left);
        int[] right = calculate(root.right);
        int[] res = new int[2];
        
        res[0] = root.val + left[1] + right[1]; //robbed root
        res[1] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]); //not robbed
        
        return res;
    }
}