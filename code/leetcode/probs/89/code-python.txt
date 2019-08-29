class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        total = 1 << n
        
        res = [0]
        shift = 1
        while len(res) != total:
            res += [x + shift for x in res[::-1]] 
            shift *= 2
        
        return res