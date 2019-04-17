class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = [0]* (max(days)+1)
        daySt = set(days)
        
        for i in range(days[0], days[-1]+1):
            if i in daySt:
                dp[i] = min(dp[i-1] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
            else:
                dp[i] = dp[i-1]
                    
        return dp[-1]