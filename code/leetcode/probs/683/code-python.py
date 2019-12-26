# O(N^2) Binary Search Solution
from bisect import bisect_left as bl
class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        
        res = [float('-inf'), float('inf')]
        
        for day, loc in enumerate(bulbs):
            index = bl(res, loc)
            if loc - res[index-1] - 1 == K or res[index] - loc - 1== K:
                return day + 1
            res.insert(index, loc)
        return -1
        
# O(N) LinkedList Solution
class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        garden = [[i - 1, i + 1] for i in range(len(flowers))]
        garden[0][0], garden[-1][1] = None, None
        ans = -1
        for i in range(len(flowers) - 1, -1, -1):
            cur = flowers[i] - 1
            left, right = garden[cur]
            if right != None and right - cur == k + 1:
                ans = i + 1
            if left != None and cur - left == k + 1:
                ans = i + 1
            if right != None:
                garden[right][0] = left
            if left != None:
                garden[left][1] = right
        return ans
        
# O(N) Sliding Windows Solution (to be added)