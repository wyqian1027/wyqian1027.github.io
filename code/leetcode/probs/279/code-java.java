// Only need to check i - squares in the cache!
class Solution {
    public int numSquares(int n) {
        
        int[] cache = new int[n+1];
        Arrays.fill(cache, -1);
        cache[0] = 0;
        
        for (int i = 1; i <= n; i++) {
            int res = Integer.MAX_VALUE;
            int x = 1;
            while (i - x*x >= 0) {
                res = Math.min(res, cache[i - x*x] + 1);
                x++;
            }
            cache[i] = res;
        }
        
        return cache[n];
    }
}