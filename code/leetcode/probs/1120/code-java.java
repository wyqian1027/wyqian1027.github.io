class Solution {
    public double maximumAverageSubtree(TreeNode root) {
        return helper(root)[0];
    }
    
    public double[] helper(TreeNode root) {
        if (root == null) return new double[]{Double.MIN_VALUE, 0.0, 0.0}; // avg, count, total
        double[] left  = helper(root.left);
        double[] right = helper(root.right);
        double count = left[1] + right[1] + 1;
        double total = left[2] + right[2] + root.val;
        double avg = Math.max(Math.max(left[0], right[0]), total / count);
        return new double[]{avg, count, total};
    }
}