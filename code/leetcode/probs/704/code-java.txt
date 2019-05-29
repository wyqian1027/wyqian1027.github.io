class Solution {
    public int maxProfit(int[] p, int fee) {
        
        if (p.length<=1) return 0;
        
        // int[] dp = new int[p.length];
        int min = p[0];
        int profit = 0;
        
        for(int i = 1; i < p.length; i++){
            min = Math.min(min,p[i-1]-profit);
            profit = Math.max(profit, p[i]-fee-min);
        }
        
        return profit;
    }
}