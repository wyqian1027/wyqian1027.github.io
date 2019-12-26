class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        S = S.replace("-", "").upper()
        n = len(S)
        first = n % K
        res = []
        if first: res.append(S[:first])
        for i in range(first, n, K):
            res.append(S[i:i+K])
        return "-".join(res)
        
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        
        S = S.replace("-", "")[::-1].upper()
        return "-".join([S[i:i+K] for i in range(0, len(S), K)])[::-1]
            
        
        