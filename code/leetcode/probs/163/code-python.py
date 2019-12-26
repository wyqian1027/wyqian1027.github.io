class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def stringify(l, r):
            return str(l) if l == r else str(l)+"->"+str(r)

        l = lower
        res = []
        if not nums: return [stringify(lower, upper)]
        
        for i, num in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if l != num:
                res.append(stringify(l, num-1))
            l = num + 1
        if l <= upper:
            res.append(stringify(l, upper))
            
        return res