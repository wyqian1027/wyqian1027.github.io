# 1. Recursion: O(2^(T+P))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        if not p and not s:
            return True
       
        if not p and s:
            return False
        
        firstMatch = len(s) > 0 and (p[0] == s[0] or p[0] == '.')
        
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or \
                   (firstMatch and self.isMatch(s[1:], p))
        else:
            return firstMatch and self.isMatch(s[1:], p[1:])

# 1. DP  O(TP)

class Solution:
    
    def isMatch(self, text, pattern):

        memo = {}
        
        def calculate(i, j):
            
            if (i, j) in memo: return memo[(i,j)]
            
            # pattern ends, text must end
            if j == len(pattern):
                ans = (i == len(text))
            
            else:
                
                curMatch = i < len(text) and (pattern[j] == text[i] or pattern[j] == '.')
                
                if j + 1 < len(pattern) and pattern[j+1] == '*':
                    
                    # curMatch matches so check next text. j stays because text[i+1] could be duplicated
                    ans = curMatch and calculate(i+1, j)
                    
                    # curMatch does not match, use this * to erase j-th pattern
                    ans = ans or calculate(i, j+2)
                
                else:
                    
                    ans = curMatch and calculate(i+1, j+1)
                    
            memo[(i,j)] = ans
            
            return ans
        
        return calculate(0,0)
            