// Standard Two-Pointers
class Solution {
    public int[] twoSum(int[] A, int target) {
        
        int i = 0, j = A.length - 1;
        int[] res = new int[2];
        
        while (i < j){
            if (A[i] + A[j] == target){
                res[0] = i+1;
                res[1] = j+1;
                return res;
            } else if (A[i] + A[j] < target) {
                i += 1;
            } else {
                j -= 1;
            }
        }
        return res;
    }
}