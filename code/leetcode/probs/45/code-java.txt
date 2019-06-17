// Two pointers O(N), BFS structure

lass Solution {
    public int jump(int[] nums) {
 
        int n = nums.length;
        int count = 0;
        int right = 0;
        int left = 0;
        
        for (int i = 0; i < n - 1; i++){
            right = Math.max(right, nums[i] + i);
            if (i >= left) {
                left = right;
                count++;
            }
        }
        return count;
    }
}