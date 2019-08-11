class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = [0]*26
        valids = [0]*26
        for ch in S:
            counts[ord(ch) - ord("a")] += 1
        
        res = ""
        for i in range(len(S)):
            maxCount = 0
            cand = -1
            for j in range(len(counts)):
                if counts[j] > maxCount and i >= valids[j]:
                    maxCount = counts[j]
                    cand = j
            if cand == -1: return ""
            ch = chr(cand + ord("a"))
            res += ch
            valids[cand] = i + 2
            counts[cand] -= 1
        
        return res