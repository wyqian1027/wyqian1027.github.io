class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        tot = 0
        for x in nums:
            tot ^= x
        
        tot = tot & ~(tot - 1) # extract last set bit
        
        res = [0, 0] # divide into two categories
        for x in nums:
            if x & tot == 0:
                res[0] = res[0]^x
            else:
                res[1] = res[1]^x
        
        return res
        