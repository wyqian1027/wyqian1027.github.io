class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        
        N = 0
        
        for i, ch in enumerate(S):
            if ch.isdigit():
                N *= int(ch)
            else:
                N += 1
            if N >= K: break
        
        for j in range(i, -1, -1):
            if S[j].isdigit():
                N //= int(S[j])
                K = K % N
            else:
                if K == 0 or K == N:
                    return S[j]
                N -= 1