// 1. Make Array Copy
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        
        if (nums == null || nums.length == 0) return null;
        
        int ind = nums.length / 2;
        TreeNode root = new TreeNode(nums[ind]);
        root.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, ind));
        root.right = sortedArrayToBST(Arrays.copyOfRange(nums, ind + 1, nums.length));
        
        return root;
    }
}

// 2. Track Only Indices:
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        
        return aux(nums, 0, nums.length);
    }
    
    public TreeNode aux(int[] nums, int lo, int hi) {
        
        if (nums == null || nums.length == 0) return null;
        
        if (lo >= hi) return null;
        
        int mid = lo + (hi - lo) / 2;
        
        TreeNode root = new TreeNode(nums[mid]);
        root.left = aux(nums, lo, mid);
        root.right = aux(nums, mid + 1, hi);
        
        return root;        
    }
}
