# 1. Naive solution is O(N)
# 2. Implementing SegmentTree or Binary Index Tree, reduce to O(NlgN)

class Node:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None

class SegmentTree:
        
    def __init__(self, nums):
        self.root = self.buildTree(nums, 0, len(nums) - 1)
        
        
    def buildTree(self, nums, start, end):
        
        if start > end: 
            return None
        
        elif start == end:
            node = Node(start, end)
            node.sum = nums[start]
            return node
    
        else:
            node = Node(start, end)
            mid = (start + end )//2
            node.left = self.buildTree(nums, start, mid)
            node.right = self.buildTree(nums, mid+1, end)
            node.sum = node.left.sum + node.right.sum
            return node
    
    def getSumRange(self, start, end, cur):
        
        # more intuitive
        if not cur or cur.end < start or cur.start > end: 
            return 0
        elif start <= cur.start and cur.end <= end:
            return cur.sum
        else:
            return self.getSumRange(start, end, cur.left) + self.getSumRange(start, end, cur.right)
            
        # propagate from leaves
        # if cur.start == start and cur.end == end:
        #     return cur.sum
        # else:
        #     mid = (cur.start + cur.end) // 2
        #     if end <= mid:
        #         return self.getSumRange(start, end, cur.left)
        #     elif start > mid:
        #         return self.getSumRange(start, end, cur.right)
        #     else:
        #         return self.getSumRange(start, mid, cur.left) + self.getSumRange(mid+1, end, cur.right)
    
    def update(self, ind, val):
        self.updateHelper(ind, val, self.root)
        
    def updateHelper(self, ind, val, cur):
        
        if cur.start == cur.end:
            cur.sum = val
            return
        mid = (cur.start + cur.end) // 2
        if ind <= mid:
            self.updateHelper(ind, val, cur.left)
        else:
            self.updateHelper(ind, val, cur.right)
        cur.sum = cur.left.sum + cur.right.sum
        
class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = SegmentTree(nums)

    def update(self, i: int, val: int) -> None:
        self.tree.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.tree.getSumRange(i, j, self.tree.root)
        
# 3. Binary Index Tree

class BinaryIndexTree:
    
    def __init__(self, nums):
        self.BIT = [0]*(len(nums) + 1)
        self.nums = [0]*len(nums)
        for i, v in enumerate(nums):
            self.update(i, v)
    
    def _lowbit(self, a):
        return a & -a
    
    def update(self, i, v):
        diff = v - self.nums[i]
        self.nums[i] = v
        i += 1
        while i <= len(self.nums):
            self.BIT[i] += diff
            i += self._lowbit(i)
    
    def getSum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.BIT[i]
            i -= self._lowbit(i)
        return s

class NumArray:

    def __init__(self, nums: List[int]):
        self.BIT = BinaryIndexTree(nums)

    def update(self, i: int, val: int) -> None:
        self.BIT.update(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.BIT.getSum(j) - self.BIT.getSum(i-1)