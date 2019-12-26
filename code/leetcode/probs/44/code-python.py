# DP similar to #10
class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}
        
        def calculate(i, j):
            
            if (i, j) in memo: return memo[(i, j)]
            
            if j == len(p):
                ans = (i == len(s))
            else:
                firstMatch = (i < len(s)) and p[j] in {'?', s[i]}
                if p[j] == '*':
                    ans = calculate(i, j+1) or (i < len(s) and calculate(i+1, j))
                else:
                    ans = firstMatch and calculate(i+1, j+1)
                    
            memo[(i,j)] = ans
            return ans
        
        return calculate(0, 0)
            