// Using Stack and Dictionary
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        
        lastIndex = {}
        stack = []
        
        for i, v in enumerate(text):
            lastIndex[v] = i
        
        for i, ch in enumerate(text):
            if ch in stack:
                continue
            while stack and stack[-1] > ch and lastIndex[stack[-1]] > i:
                stack.pop()
            stack.append(ch)

        return "".join(stack)