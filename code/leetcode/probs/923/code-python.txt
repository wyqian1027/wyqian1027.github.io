# 1. O(N^2), in place

class Solution:

    def threeSumMulti(self, A: List[int], target: int) -> int:
               
        MOD = pow(10, 9) + 7
        A.sort()
        ans = 0
        
        for i in range(len(A) - 2):
        
            left, right = i + 1, len(A) - 1
            
            while left < right:
                
                s = A[i] + A[left] + A[right]  
                
                if s > target:
                    right -= 1
                    
                elif s < target:
                    left += 1
                    
                elif A[left] != A[right]:
                    nleft = nright = 1
                    while left < right and A[left] == A[left+1]:
                        left += 1
                        nleft += 1
                    while left < right and A[right] == A[right-1]: 
                        right -= 1
                        nright += 1
                    ans += nleft*nright
                    ans %= MOD
                    
                    left += 1
                    right -= 1
                else:
                    ans += (right-left+1)*(right-left)//2
                    ans %= MOD
                    break
            
        return ans

# 2. O(N + const)

class Solution:

    def threeSumMulti(self, A, target):
    
        c = collections.Counter(A)
        
        res = 0
        
        for i, j in itertools.combinations_with_replacement(c, 2):
        
            k = target - i - j
            
            if i == j == k: 
                res += c[i] * (c[i] - 1) * (c[i] - 2) // 6
            
            elif i == j != k: 
                res += c[i] * (c[i] - 1) // 2 * c[k]
            
            elif k > i and k > j: 
                res += c[i] * c[j] * c[k]
            
        return res % (10**9 + 7)