class Solution1:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        
         dp = [float('inf') for _ in range(T+1)]
         dp[0] = 0
        
         for i in range(0, T+1):
             for clip in clips:
                 if clip[0] <= i <= clip[1]:
                     dp[i] = min(dp[i], dp[clip[0]]+1)
             if dp[i] == float("inf"): return -1
        
         return dp[-1]
         
class Solution2:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:      
    
        end_left, end_right, ans = -1, 0, 0
    
        for i, j in sorted(clips):
            if end_right >= T: break
            if i <= end_left:
                end_right = max(end_right, j)
            elif end_left < i <= end_right:
                end_left = end_right
                ans += 1
                end_right = j
            else:
                return -1
        
        return ans if end_right >= T else -1