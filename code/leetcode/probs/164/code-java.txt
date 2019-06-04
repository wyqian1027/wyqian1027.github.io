//1. O(NLogN)
class Solution {
    public int maximumGap(int[] nums) {
        
        if (nums.length < 2) return 0;
        
        Arrays.sort(nums);
        
        int maxD = 0;
        
        for (int i = 1; i < nums.length; i++) {
            maxD = Math.max(maxD, nums[i] - nums[i-1]);
        }
        
        return maxD;      
        
    }
}

//2. Using RadixSort O(N)
class Solution{
    public int maximumGap(int[] nums) {

        radixSort(nums);
        int maxD = 0;
        for (int i = 1; i < nums.length; i++) {
            maxD = Math.max(maxD, nums[i] - nums[i-1]);
        }
        return maxD;
    }
    
    private int getMax(int[] nums) {
        int max = 0;
        for (int x: nums) {
            max = Math.max(max, x);
        }
        return max;
    }
    
    public void radixSort(int[] nums){
        int m = getMax(nums);
        for (int exp = 1; m/exp > 0; exp *= 10) {
            countSort(nums, exp);
        }
    }
    
    private void countSort(int[] nums, int exp) {
        int n = nums.length;
        int[] output = new int[n];
        int[] count = new int[10];
        
        for (int i = 0; i < n; i++){
            count[(nums[i]/exp) % 10] += 1;
        }
        for (int i = 1; i < 10; i++){
            count[i] += count[i-1];
        }
        for (int i = n-1; i >= 0; i--){
            output[count[(nums[i]/exp) % 10]-1] = nums[i];
            count[(nums[i]/exp) % 10] -= 1;
        }
        for (int i = 0; i < n; i++){
            nums[i] = output[i];
        }       
    }
}

// 3. Bucket O(N) time, O(N) space
class Solution {
    public int maximumGap(int[] nums) {
        if (nums.length < 2) return 0;
        
        int max, min;
        max = min = nums[0];
        for (int x: nums) {
            max = Math.max(max, x);
            min = Math.min(min, x);
        }
        
        int n = nums.length - 1;
        int size = (int) Math.ceil((double)(max - min)/(nums.length - 1));
        int[] bucketMin = new int[n];
        int[] bucketMax = new int[n];
        Arrays.fill(bucketMin, Integer.MAX_VALUE);
        Arrays.fill(bucketMax, Integer.MIN_VALUE);
        
        for (int x: nums){
            if (x != max && x != max) {
                int id = (x - min) / size;
                bucketMin[id] = Math.min(bucketMin[id], x);
                bucketMax[id] = Math.max(bucketMax[id], x); 
            }
        }
        int ans = 0;
        int prev = min;
        
        for (int i = 0; i < n; i++) {
            if (bucketMin[i] == Integer.MAX_VALUE && bucketMax[i] == Integer.MIN_VALUE) {
                continue;
            }
            ans = Math.max(ans, bucketMin[i] - prev);
            prev = bucketMax[i];
        }
        
        ans = Math.max(max - prev, ans);
        return ans;
    }
}