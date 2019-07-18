# 1. MergeSortAndCount O(NlgN) Brilliant solution found!
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1]+ num)
        def sort(lo, hi):
            m = (lo + hi)//2
            if m == lo:
                return 0
            count = sort(lo, m) + sort(m, hi)
            i = j = m
            for left in prefix[lo: m]:
                while i < hi and prefix[i] - left <  lower: i += 1
                while j < hi and prefix[j] - left <= upper: j += 1
                count += j - i
            prefix[lo:hi] = sorted(prefix[lo:hi])
            return count
        return sort(0, len(prefix))

# 2. O(NlgN) Using Segment Tree. Notice the usage are different.

class SegmentNode:
    def __init__(self, lo, hi):
        self.lo = lo
        self.hi = hi
        self.left = None
        self.right = None
        self.count = 0

class Solution:
    
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums: return 0
        ans = 0
        st = set()
        s = 0
        for num in nums:
            s += num
            st.add(s)
        arr = sorted(list(st))
        root = self.buildSegmentTree(arr, 0, len(arr)-1)
        for x in nums[::-1]:
            self.updateSegmentTree(root, s) 
            s -= x                           
            ans += self.getCount(root, lower+s, upper+s)
        return ans
    
        # For loop:
        # Sum of range [i ,j] = prefix[j] - prefix[i-1]
        # Want to check: prefix[j] - prefix[i-1] belong to [lower, upper]
        # Equivalently to check: prefix[j] belong to [lower + prefix[i-1], upper + prefix[i-1]]        
        
    def buildSegmentTree(self, arr, lo, hi):
        if lo > hi:
            return None
        node = SegmentNode(arr[lo], arr[hi])
        if lo == hi:
            return node
        node.left = self.buildSegmentTree(arr, lo, (lo+hi)//2)
        node.right = self.buildSegmentTree(arr, (lo+hi)//2 + 1, hi)
        return node
    
    def updateSegmentTree(self, root, val):
        if not root: return;
        if root.lo <= val <= root.hi:
            root.count += 1
            self.updateSegmentTree(root.left, val)
            self.updateSegmentTree(root.right, val)
            
    def getCount(self, root, lo, hi):
        if not root: return 0
        if root.lo > hi or root.hi < lo: return 0
        if lo <= root.lo and root.hi <= hi: return root.count
        return self.getCount(root.left, lo, hi) + self.getCount(root.right, lo, hi)
    
    