class Solution:
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        st = set(wordDict)
        d = {}
    
        def dfs(s, d):
            
            if s in d:
                return d[s]
                
            res = []
            if s == "": 
                res.append("")   #placeholder for making 'for el in sub' valid
                return res
            
            for w in st:
                if s[:len(w)] == w:
                    sub = dfs(s[len(w):], d)
                    for el in sub:
                        if el == "":
                            res.append(w)
                        else:
                            res.append(w + " " + el)
            d[s] = res
            return res
            
        return dfs(s, d)   
        
# other ways:
import functools
class Solution:    
    def wordBreak_DP_on_s(self, s: str, wordDict: List[str]) -> List[str]:
        
        # lead to TLE
        st = set(wordDict)
        dp = [True] + [False]*len(s)
        res = collections.defaultdict(list)
        res[0].append("")
        
        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in st:
                    dp[i+1] = True
                    if j == 0: 
                        res[i+1].append(s[j:i+1])
                    else:
                        for sub in res[j]:
                            res[i+1].append(sub+" "+s[j:i+1])
        return res[len(s)]
    
    
    def wordBreak_DP_on_wordDict(self, s, wordDict):
        st = set(wordDict)
        @functools.lru_cache(maxsize=None)
        def calculate(s):
            if s == "":
                return [""]
            
            ans = []
            for w in st:
                part = s[:len(w)]
                rem  = s[len(w):]
                if part == w and rem != "":
                    for sub in calculate(rem):
                        ans.append(w + " " + sub)
                elif part == w and rem == "":
                    ans.append(w)
            return ans
        return calculate(s) 