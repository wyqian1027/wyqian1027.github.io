# 1. Generic DP for any m subarrays:
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        m = 3
        acc = [0]
        dp_max = [[0]*(n+1) for _ in range(m+1)]
        dp_index = [[0]*(n+1) for _ in range(m+1)]
        
        for num in nums:
            acc.append(acc[-1] + num)
        
        for i in range(1, m+1):
            for j in range(i*k, n+1):
                if dp_max[i-1][j-k] + acc[j] - acc[j-k] > dp_max[i][j-1]:
                    dp_index[i][j] = j - k
                    dp_max[i][j] = dp_max[i-1][j-k] + acc[j] - acc[j-k]
                else:
                    dp_index[i][j] = dp_index[i][j-1]
                    dp_max[i][j] = dp_max[i][j-1]
                    
        ans = []
        loc = n
        for i in range(m, 0, -1):
            loc = dp_index[i][loc]
            ans.append(loc)
        
        return ans[::-1]


# 2. Think using Left, Middle, Right subarrays:
# Be careful with edge cases
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        pos_left  = [0]*n  # start index for left  subarray
        pos_right = [0]*n  # start index for right subarray
        acc = [0]          # accumulation array
        
        for num in nums: 
            acc.append(acc[-1] + num)
            
        total = acc[k] - acc[0]
        for i in range(k, n - 2*k + 1):
            if acc[i+1] - acc[i+1-k] > total:
                total = acc[i+1] - acc[i+1-k]
                pos_left[i] = i + 1 - k
            else:
                pos_left[i] = pos_left[i-1]

        total = acc[n] - acc[n-k]
        pos_right[n-k] = n-k
        for i in reversed(range(2*k, n - k + 1)):
            if acc[i+k] - acc[i] >= total:
                total = acc[i+k] - acc[i]
                pos_right[i] = i
            else:
                pos_right[i] = pos_right[i+1]
                
        ans = -float('inf'), 0, 0, 0
        for i in range(k, n - 2*k + 1):
            l, r = pos_left[i-1], pos_right[i+k]
            s = acc[i+k] - acc[i] + acc[l+k] - acc[l] + acc[r+k] - acc[r]
            if s > ans[0]:
                ans = s, l, i, r
        
        return ans[1:]