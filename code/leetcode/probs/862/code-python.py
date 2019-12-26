class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        
        B = [0]
        for a in A:
            B.append(B[-1] + a)
        
        ans = float('inf')
        q = collections.deque() 
        # left locations: must be of increasing accumulated sum
        # [proof by contradiction]
        
        for r, s in enumerate(B):
            
            while q and s <= B[q[-1]]:
                q.pop()           
            
            while q and s - B[q[0]] >= K:
                ans = min(ans, r - q.popleft())
            
            q.append(r)
        
        return ans if ans != float('inf') else -1