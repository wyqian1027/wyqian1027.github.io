// instead of DP with O(N) space cost, use two pointers

class Solution {
    public int minCostClimbingStairs(int[] cost) {
    
        int pre = 0, cur = 0;
        for (int i = 0; i < cost.length; i++){
            
            int nxt = Math.min(pre, cur) + cost[i];
            pre = cur;
            cur = nxt;
        }
        return Math.min(pre, cur);
    }
}