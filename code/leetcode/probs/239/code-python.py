class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = collections.deque()
        
        for i, num in enumerate(nums):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] <= num:
                q.pop()
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])
        return res