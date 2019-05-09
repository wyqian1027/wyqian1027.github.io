# O(N^2), having 0 being the constraints, reducing the complexity

class Solution:

    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        
        dic = {}
        res = 0
        
        for a in A:
            for b in B:
                if a + b in dic:
                    dic[a+b] += 1
                else:
                    dic[a+b] = 1
        
        for c in C:
            for d in D:
                if (-c - d) in dic:
                    res += dic[- c - d]
        
        return res