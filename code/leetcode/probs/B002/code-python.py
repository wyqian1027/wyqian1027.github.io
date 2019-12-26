#O(N) key is to keep track of zeros

def productOfKConsecutive(nums, k):
    res = []
    s = 1
    zeros = 0
    for i, num in enumerate(nums):
        # divide old
        if i >= k:
            if nums[i-k] == 0:
                zeros -= 1
            else:
                s //= nums[i-k]
        # multiply new
        if num == 0:
            zeros += 1
        else:
            s *= num
        # update
        if zeros > 0: 
            res.append(0)
        else:
            res.append(s)            
    return res