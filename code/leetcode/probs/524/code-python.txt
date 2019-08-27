# Do it without sorting or with sorting

class Solution:
    def findLongestWord2(self, s: str, d: List[str]) -> str:
        
        cand = -1
        longest = 0
        
        for index, word in enumerate(d):
            i = j = 0
            while i < len(s):
                if s[i] == word[j]:
                    j += 1
                    if j >= len(word):
                        if len(word) > longest:
                            cand = index
                            longest = len(word)
                        elif len(word) == longest and word < d[cand]:
                            cand = index
                        break
                i += 1

        
        return d[cand] if cand != -1 else ""
    
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        
        d.sort(key=lambda word: (-len(word), word))
        
        for word in d:
            i = j = 0
            while i < len(s):
                if s[i] == word[j]:
                    j += 1
                    if j >= len(word):
                        return word
                i += 1
        
        return ""
        
        