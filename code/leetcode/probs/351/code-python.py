class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        if n < m: return 0
        self.count = 0
        self.locs = set([(x, y) for x in range(3) for y in range(3)])
        self.dfs([False]*9, -1, -1, 0, m, n)
        return self.count

    def dfs(self, visited, prevR, prevC, whichKey, minKey, maxKey):
        
        if whichKey > maxKey:
            return
        
        if minKey <= whichKey <= maxKey:
            self.count += 1
            
        for i in range(len(visited)):
            if not visited[i]: 
                curR, curC = i // 3, i % 3
                mR, mC = (curR + prevR) / 2.0, (curC + prevC) / 2.0
                if prevR != -1 and (mR, mC) in self.locs and visited[int(mR*3+mC)] == False:
                    continue
                visited[i] = True
                self.dfs(visited, curR, curC, whichKey+1, minKey, maxKey)
                visited[i] = False