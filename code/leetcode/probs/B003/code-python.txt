# reuse LIS codes to update length of LIS
# along with prev, index for returning the LIS sequence

def getSubsequenceOfSizeK(nums, k):
    dp = []      # for look up LIS table
    prev = {}    # storing nodes, like LinkedList
    index = []   # map from val in dp table to index
    for i, num in enumerate(nums):
        idx = bl(dp, num)
        if idx == len(dp):
            dp.append(num)
            index.append(i)
        else:
            dp[idx] = num
            index[idx] = i
        prev[i] = index[idx - 1] if idx != 0 else None
        if len(dp) == k:
            break
    res = []
    while i:
        res.append(nums[i])
        i = prev[i]
    return res[::-1]