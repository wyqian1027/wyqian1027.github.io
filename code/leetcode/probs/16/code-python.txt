class Solution:
    def threeSumClosest(self, A, target):
        
        A.sort()
        if sum(A[:3]) > target: return sum(A[:3])
        if sum(A[-3:]) < target: return sum(A[-3:])
        
        dist = float('inf')
        ans = A[:3]
        
        for i in range(len(A)-2):
            if i != 0 and A[i] == A[i-1]: continue
                
            l, r = i + 1, len(A) - 1
            while l < r:
                s = A[i] + A[l] + A[r]
                if s == target:
                    return target
                elif abs(s - target) < dist:
                    ans = s
                    dist = abs(s-target)
                elif s > target:
                    r -= 1
                else:
                    l += 1
        return ans