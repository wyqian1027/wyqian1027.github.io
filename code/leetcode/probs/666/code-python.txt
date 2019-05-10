# 1. Level by level

class Solution:

    def pathSum(self, A):
        
        if not A: return 0
        if len(A) == 1: return A[0] % 10
        
        q = collections.deque(A)
        q.popleft()
        level = [A[0] % 10]
        newLevel = [False, False]
        curDepth = 2
        lastInd = 0 
        s = 0
        
        while q:
            x = q.popleft()
            depth, pos, val = x // 100, (x//10) % 10, x % 10
            if depth != curDepth:
                s += sum(level[i] for i in range(len(level)) if level[i] != False and \
                        newLevel[2*i] == False and newLevel[2*i+1] == False)
                curDepth += 1
                level = newLevel
                newLevel = [False]*((curDepth-1)**2)
                newLevel[pos-1] = level[(pos-1)//2] + val
                
            newLevel[pos-1] = level[(pos-1)//2] + val    
            lastInd = pos
        
        return s + sum(newLevel) + sum(level[i] for i in range(len(level)) if level[i] != False and \
            newLevel[2*i] == False and newLevel[2*i+1] == False)

# 2. Elegant DFS

class Solution:

    def pathSum(self, A):
        
        if not A: return 0
        if len(A) == 1: return A[0] % 10
        
        values = {x // 10: x % 10 for x in A}
        self.s = 0
        
        def dfs(node, curSum):
            
            if node not in values: return
            curSum += values[node]
            depth, pos = divmod(node, 10)
            
            left = (depth + 1)*10 + 2*pos -1
            right = left + 1
            
            if left not in values and right not in values:
                self.s += curSum
            else:
                dfs(left, curSum)
                dfs(right, curSum)
        
        dfs(A[0]//10, 0)
        
        return self.s
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        