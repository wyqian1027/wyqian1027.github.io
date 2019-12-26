class Solution {

// 1. O(NLogN) time, O(1) space

    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) return 0;
        
        Arrays.sort(nums);
               
        int max = 1;
        int cur = 1;
        
        for (int i=1; i < nums.length; i++) {
            if (nums[i] != nums[i-1]) {
                if (nums[i] - 1 == nums[i-1]) {
                    cur += 1;
                } else {
                    cur = 1;
                }
                max = Math.max(max, cur);
            }
        }
        
        return max;      
    }

// 2. O(N) time, O(N) space

    public int longestConsecutive(int[] nums) {
        
        Set<Integer> st = new HashSet<>();
        int max = 0;

        for (int x: nums) {
            st.add(x);
        }
        for (int x: nums) {
            if (!st.contains(x-1)){
                int cur = 1;
                while (st.contains(x+1)) {
                    cur += 1;
                    x += 1;
                }
                max = Math.max(max, cur);               
                
            }
        }
        
        return max;  
    }
}