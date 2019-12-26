class Solution:
    def generate(self, n: int) -> List[List[int]]:        
        arr = []
        res = []
        for i in range(1, n+1):
            arr += [1]
            for j in range(i-2, 0, -1):
                arr[j] = arr[j] + arr[j-1]
            res.append(arr[:])
        return res
        
# BEtter clarity:
class Solution:
    def generate(self, n):
        if n <= 0: return []
        res = [[1]]
        while n > 1:
            prev = res[-1]
            new = [1] + [prev[i]+prev[i+1] for i in range(0, len(prev)-1)] + [1]
            res.append(new)   
            n -= 1
        return res