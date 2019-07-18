class Solution:
    
    def maxNumber(self, A: List[int], B: List[int], k: int) -> List[int]:
    
        ans = [0]*k
        for left in range(0, k+1):
            right = k - left
            if left <= len(A) and right <= len(B):
                a = self.maxNumberFromOne(A, left)
                b = self.maxNumberFromOne(B, right)
                ans = max(self.merge(a, b), ans)
        return ans
    
    def merge(self, A, B):
        res = []
        while A or B:
            if A > B:
                res.append(A[0])
                A = A[1:]
            else:
                res.append(B[0])
                B = B[1:]
        return res
    
    def maxNumberFromOne(self, A, k):
        num = []
        n = len(A)
        start = 0
        for need in range(k, 0, -1):
            cur = 0
            for j in range(start, n - need + 1):
                # if j + need > n: # big improvement
                #     break
                if A[j] > cur:
                    cur = A[j]
                    start = j
            num.append(cur)
            start += 1
        return num
    
    # Some cool functions to use
    
    # def merge(self, a, b):
    #     return [max(a, b).pop(0) for _ in a+b]
    
    # def maxNumberFromOne(self, nums, k):
    #     to_drop = len(nums) - k
    #     res = []
    #     for num in nums:
    #         while to_drop and res and res[-1] < num:
    #             res.pop()
    #             to_drop -= 1
    #         res.append(num)
    #     return res[:k]