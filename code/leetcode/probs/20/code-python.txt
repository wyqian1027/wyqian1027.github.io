class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {"(": ")",
             "{": "}",
             "[": "]"}
        
        stack = []
        
        for ch in s:
            if ch in d:
                stack.append(ch)
            else:
                if stack and d[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
        
        return not stack
        