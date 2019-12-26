class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        Arrays.sort(nums);
        int nearest = nums[0]+nums[1]+nums[2];
        int l, r, s;
        for (int i=0; i<nums.length-2; i++){
            if (i>0 && nums[i] == nums[i-1]) continue;
            l = i+1;
            r = nums.length-1;
            while (l < r){
                s = nums[i] + nums[l] + nums[r];
                if (s == target) {
                    return target;
                } else {
                    if (Math.abs(s-target) < Math.abs(nearest-target)){
                        nearest = s;
                    }                    
                    if (s > target) {
                        r--;
                    } else {
                        l++;
                    }                  
                }
            }
        }
        return nearest;
    }
}