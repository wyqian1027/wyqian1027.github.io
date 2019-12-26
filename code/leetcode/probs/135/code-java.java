// O(N) time, O(N) space solution

class Solution {
    public int candy(int[] ratings) {
       
        int n = ratings.length;
        int[] leftArr = new int[n];
        int[] rightArr = new int[n];
        
        Arrays.fill(leftArr, 1);
        Arrays.fill(rightArr, 1);
        
        for (int i = 1; i < n; i++){
            if (ratings[i] > ratings[i-1]){
                leftArr[i] = leftArr[i-1] + 1;
            }
        }
        
        for (int i = n-2; i >= 0; i--){
            if (ratings[i] > ratings[i+1]){
                rightArr[i] = rightArr[i+1] + 1;
            }
        }
        
        int ans = 0;
        for (int i = 0; i < n; i++){
            ans += Math.max(leftArr[i], rightArr[i]);
        }
        return ans;
    }
}