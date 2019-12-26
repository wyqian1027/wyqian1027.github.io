class Solution {
    public int climbStairs(int n) {
        
        int pre = 1, cur = 2;
        if (n == 1) return pre;
        
        for (int i = 2; i < n; i++){
            int nxt = pre + cur;
            pre = cur;
            cur = nxt;
        }
        return cur;
    }
}