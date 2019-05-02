#1. Backtracking Solution
class Solution:
    def readBinaryWatch(self, n):
        
        res = []
        
        def dfs(n, hr, mn, idx, res):
            
            if hr > 11 or mn > 59: return
            
            if n == 0:
                res.append("{}:{:02d}".format(hr, mn))
                return
            
            for i in range(idx, 10):
                if i < 4:
                    dfs(n-1, hr + (1 << i), mn, i+1, res)
                else:
                    k = i - 4
                    dfs(n-1, hr, mn + (1 << k), i+1, res)
        
        dfs(n, 0, 0, 0, res)
        
        return res
        
#2. Iterating all hours/minutes:

class Solution:
    def readBinaryWatch(self, n):
        
        res = []
        
        for hr in range(0, 12):
            for mn in range(0, 60):
                if bin(mn).count('1') + bin(hr).count('1') == n:
                    res.append("{}:{:02d}".format(hr, mn))
        
        return res