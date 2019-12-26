class Solution:
    def lengthLongestPath(self, inputs: str) -> int:
        
        inputs = inputs.split("\n")
        stack = []
        maxLen = 0;

        for path in inputs:

            level = path.count("\t")
            while stack and level < len(stack):
                stack.pop()

            file = path[level:]
            if "." in file:
                maxLen = max(maxLen, len(file) +sum(stack))
            else:
                stack.append(len(file)+1)
    
        return maxLen
        
        
// or
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        input = input.split("\n")
        stack = []     # Record directories: level, and its current length
        maxSofar = 0
        
        for item in input:
            level = item.count("\t")
            while stack and level <= stack[-1][0]:
                stack.pop()
            
            prev = stack[-1][1] if stack else 0
            if "." not in item:
                stack.append([level, prev + len(item) - level + 1])
            else:
                maxSofar = max(maxSofar, prev + len(item) - level)
        return maxSofar