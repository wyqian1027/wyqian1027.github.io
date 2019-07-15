# TIP: instead of division use fraction representation to avoid precision problem
# duplicates are allowed!
# for each point, make a dictionary of all possible slopes
# O(N^2) time complexity

class Solution:
    
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)
        
        def frac(x,y):
            g = gcd(x,y)
            return x//g, y//g
            
        def slope(A, B):
            if A[0] == B[0]:
                return float('inf')
            elif A[1] == B[1]:
                return 0
            else:
                return frac((A[1] - B[1]),(A[0] - B[0]))      
        
        n = len(points)
        if n <= 2: return n
        maxP = 0
        
        for i in range(n-1):
            d = {float('inf'): 1}
            same = 0
            curM = 1
            for j in range(i+1, n):   
                A, B = points[i], points[j]
                if A == B: 
                    same += 1
                    continue
                s = slope(A, B)
                # print(s)
                if s not in d:
                    d[s] = 1
                d[s] += 1
                if d[s] > curM: curM = d[s]
            maxP = max(maxP, curM + same)
        
        return maxP