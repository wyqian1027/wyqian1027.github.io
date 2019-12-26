import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        ans = ""
        nums = list(range(1, n+1))
        
        k -= 1
        for _ in range(n):
            index, rem = divmod(k, math.factorial(n-1))
            k = rem
            ans += str(nums[index])
            nums.pop(index)
            n -= 1
            
        return ans