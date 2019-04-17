class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        Set<Integer> set = new HashSet<>();
        int lastDay = days[days.length-1];
        int[] dp = new int[lastDay + 1];

        for (int d: days){
            set.add(d);
        }
        
        for (int i=days[0]; i <= lastDay; i++){
            if (set.contains(i)){
                dp[i] = dp[i-1] + costs[0];
                dp[i] = Math.min(dp[i], dp[Math.max(0, i-7)] + costs[1]);
                dp[i] = Math.min(dp[i], dp[Math.max(0, i-30)] + costs[2]);
            } else {
                dp[i] = dp[i-1];
            }
        }
        return dp[lastDay];
    }
}