// O(N) Use HashMap

class Solution {
    
    public int[] intersect(int[] nums1, int[] nums2) {
        
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer> arr = new LinkedList<>();
        
        for (int x: nums1) map.put(x, map.getOrDefault(x, 0) + 1);
        
        
        for (int y: nums2) {
            if (map.containsKey(y) && map.get(y) > 0) {
                arr.add(y);
                map.put(y, map.get(y)-1);
            }
        }
        
        int[] res = new int[arr.size()]; int i = 0;
        for (Integer x: arr){
            res[i++] = x;
        }
        return res;        
        
    }
}

// O(NlogN) First Sort then Two Pointers

class Solution {

    public int[] intersect(int[] nums1, int[] nums2) {
        
        if (nums1.length == 0 || nums2.length == 0) return new int[]{};
        
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        List<Integer> arr = new LinkedList<>();
        
        int p1 = 0, p2 = 0;
        while (p1 < nums1.length && p2 < nums2.length){
            
            if (nums1[p1] == nums2[p2]) {
                arr.add(nums1[p1]);
                p1++;
                p2++;
            } else if (nums1[p1] > nums2[p2]){
                p2++;
            } else {
                p1++;
            }
        }
        
        int[] res = new int[arr.size()]; int i = 0;
        for (Integer x: arr){
            res[i++] = x;
        }
        return res;
            
    }
}