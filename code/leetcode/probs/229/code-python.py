# Improved Boyer-Moore

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        cand1, cand2, count1, count2 = 0, 1, 0, 0
        
        for x in nums:
            if x == cand1:
                count1 += 1
            elif x == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = x
                count1 += 1
            elif count2 == 0:
                cand2 = x
                count2 += 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        
        return [x for x in (cand1, cand2) if nums.count(x) > len(nums)//3]