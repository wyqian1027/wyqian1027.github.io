# 1. Heap Solution O(NlgN)
from heapq import heappop, heappush

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        cand = [(l, -h, r) for l, r, h in buildings]   # - h for max heap
        cand += [(r, 0, 0) for l, r, h in buildings]   # we want all boundary points, both left and right
        cand.sort()
        
        res = [[0, 0]]           # result elements = [ position, height ]
        h = [(0, float("inf"))]    # heap elements = (- height, end position)
        
        for pos, negH, end in cand:
            
            # 1. pop all finished buildings
            while h[0][1] <= pos: heappop(h)
            
            # 2. push all starting buildings
            if negH != 0: heappush(h, (negH, end))
                
            # 3. add to result if new max is found
            if res[-1][1] != -h[0][0]:
                res.append([pos, -h[0][0]])
        
        return res[1:]
        
# 2. MergeSort-like Solution O(NlgN)
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        n = len(buildings)
        
        if n == 0:
            return []
        if n == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        
        left = self.getSkyline(buildings[:n//2])
        right = self.getSkyline(buildings[n//2:])
        
        return self.merge(left, right)
    
    def append_res(self, res, start, end, arr, curH):
        
        while start < end:
            x, y = arr[start]
            start += 1
            if y != curH:
                curH = y
                self.update_res(res, x, y)
        
        
    def update_res(self, res, x, y):
        
        if not res or res[-1][0] != x:
            res.append([x, y])
        else:
            res[-1][1] = y
            
    def merge(self, leftArr, rightArr):
        
        res = []
        leftPtr, rightPtr = 0, 0
        leftEnd, rightEnd = len(leftArr), len(rightArr)
        
        x, y = 0, 0
        leftH, rightH = 0, 0
        
        while leftPtr < leftEnd and rightPtr < rightEnd:
            
            leftElememt, rightElement = leftArr[leftPtr], rightArr[rightPtr]
            
            if leftElememt[0] < rightElement[0]:
                x, leftH = leftElememt
                leftPtr += 1
            else:
                x, rightH = rightElement
                rightPtr += 1
        
            maxH = max(leftH, rightH)
            
            if maxH != y:
                y = maxH
                self.update_res(res, x, y)
    
        self.append_res(res, leftPtr, leftEnd, leftArr, y)
        
        self.append_res(res, rightPtr, rightEnd, rightArr, y)
        
        return res