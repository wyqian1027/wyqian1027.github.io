class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        if (nums == null || nums.length == 0) return null;
        return helper(nums, 0, nums.length - 1);
    }
    
    private TreeNode helper(int[] nums, int l, int r) {
                
        if (l > r) return null;
        
        int max = nums[l], loc = l;
        for (int i = l; i <= r; i++){
            if (nums[i] > max) {
                max = nums[i];
                loc = i;
            }
        }
        
        TreeNode root = new TreeNode(max);
        root.left  = helper(nums, l, loc - 1);
        root.right = helper(nums, loc + 1, r);
        return root;
    }
}