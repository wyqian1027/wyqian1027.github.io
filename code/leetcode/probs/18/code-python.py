# Implementing n-Sum by DFS

class Solution:

    def fourSum(self, A, target):
        
        res = []
        A.sort()
        self.nSum(4, A, target, [], res)
        return res
        
    def nSum(self, n, A, target, path, res):
        
        if len(A) < n: return []
        if sum(A[-n:]) < target or sum(A[:n]) > target: return [] 
        
        if n == 3:
            
            for i in range(len(A) - 2):
                if i != 0 and A[i] == A[i-1]:
                    continue

                left, right = i + 1, len(A) - 1

                while left < right:

                    s = A[i] + A[left] + A[right]    

                    if s > target:
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        res.append(path + [A[i], A[left], A[right]])

                        while left < right and A[left] == A[left+1]:
                            left += 1
                        while left < right and A[right] == A[right-1]: 
                            right -= 1

                        left += 1
                        right -= 1
        else:
            
            for i in range(len(A) - n + 1):
                if i != 0 and A[i] == A[i-1]:
                    continue
                self.nSum(n-1, A[i+1:], target - A[i], path + [A[i]], res)
        
        
        

       