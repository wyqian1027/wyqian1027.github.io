// 1. Using Array as HashTable O(N)

class Solution {
    public int findDuplicate(int[] nums) {
        int n = nums.length;
        
        for (int i = 0; i < n; i++){
            nums[nums[i] % n] += n;
        }
        for (int i = 0; i < n; i++){
            if (nums[i] / n >= 2){
                return i;
            }
        }
        
        return -1;
    }
}

// 2. Cycle Detection O(N)
class Solution {
    public int findDuplicate(int[] nums) {
        int slow = nums[0];
        int fast = nums[0];
        
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);
        
        slow = nums[0];
        while (slow != fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return slow; 
    }
}