class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    
        stack = []
        j = 0
        for e in pushed:
            stack.append(e)
            while stack and popped and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)