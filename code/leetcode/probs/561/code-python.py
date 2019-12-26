# O(N) solution
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        count = [0]*20001
        for num in nums:
            count[num+10000] += 1
        
        total = 0
        adjust = False
        for i, freq in enumerate(count):
            if not freq: continue
            freq = freq - 1 if adjust else freq
            if freq % 2 == 0:
                total += (freq // 2)*(i-10000)
                adjust = False
            else:
                total += (freq // 2 + 1)*(i-10000)
                adjust = True
        
        return total