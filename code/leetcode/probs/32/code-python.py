# DP Solution O(N)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        dp = [0]*(len(s)+1)
        maxL = 0
        
        for i in range(1, len(s)):
        
            idx = i + 1 #index used for dp
            
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[idx] = dp[idx-2] + 2
                elif i - dp[idx-1] > 0 and s[i - dp[idx-1] - 1] == "(":
                    dp[idx] = dp[idx-1] + 2 + dp[idx - dp[idx-1] - 2]
                maxL = max(maxL, dp[idx])
        return maxL

# Stack Solution O(N) tracking last index
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [] # record locations
        stack.append(-1)
        max_length = 0
        
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                if stack: stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length
    
# Forward/Backward Traversal O(N) AND O(1) Space!
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        left = right = 0
        max_length = 0
        
        for ch in s:
            if ch == "(":
                left += 1
            else: 
                right += 1
            if left == right:
                max_length = max(max_length, left + right)
            elif right > left:
                left = right = 0
        
        left = right = 0
        for ch in reversed(s):
            if ch == "(":
                left += 1
            else: 
                right += 1
            if left == right:
                max_length = max(max_length, left + right)
            elif left > right:
                left = right = 0
        
        return max_length