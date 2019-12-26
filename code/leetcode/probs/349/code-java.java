// 1. Using Binary Search

class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        Set<Integer> set = new HashSet<>();
        
        Arrays.sort(nums1);
        
        for (int x: nums2){
            if (binarySearch(nums1, x)) {
                set.add(x);
            }
        }
        
        int[] res = new int[set.size()]; int i = 0;
        for (Integer x: set){
            res[i++] = x;
        }
        
        return res;   
    }
    
    private boolean binarySearch(int[] nums, int target){
        
        int lo = 0, hi = nums.length - 1;
        
        while (lo <= hi) {
            
            int m = lo + (hi - lo) / 2;
            
            if (target == nums[m]) {
                return true;
            } else if (target < nums[m]) {
                hi = m - 1;
            } else {
                lo = m + 1;
            }
        }
        return false;
    }
}

//2. Using HashSet
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        
        for (int x: nums1) set1.add(x);
        for (int x: nums2) set2.add(x);
        
        set1.retainAll(set2);
        
        int[] res = new int[set1.size()];
        int i = 0;
        for (Integer x: set1){
            res[i++] =  x;
        }
        
        return res;
    }
}