# 1. Recursion O(N)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        if root:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return 0

# 2. Binary Search O(LgN)

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        d = self.getDepth(root)
        if d == 0:
            return 1
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left  = pivot + 1
            else:
                right = pivot - 1
        return (2**d - 1) + left
        
    def getDepth(self, root):
        d = 0
        while root.left:
            d += 1
            root = root.left
        return d
    
    def exists(self, idx, d, root):
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                root = root.left
                right = pivot
            else:
                root = root.right
                left = pivot + 1
        return root is not None
        
# 3 Bit Mask Binary Search
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def count_level(root):
            level = 0
            while root:
                level += 1
                root = root.left
            return level - 1
        
        n = count_level(root)
        # mnust be between [2**n, 2**(n+1) -1] nodes
        
        if n == -1: return 0
        
        mask = 1 << n
        lo, hi = 2**n, 2**(n+1) - 1
        while lo <= hi:
            m = lo + (hi - lo)//2
            print(lo, hi)
            node = root
            t = m
            s = mask >> 1
            while s:
                if t & s == 0:
                    node = node.left
                else:
                    node = node.right
                s >>= 1
            if node:
                lo = m + 1
            else:
                hi = m - 1
        
        return lo - 1