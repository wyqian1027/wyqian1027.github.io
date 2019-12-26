# Not the cleanest. Passing index should give us O(N) time.
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        cur = 0
        wordLen = 0
        i = 0
        for j, word in enumerate(words):
            if cur == 0:
                cur += len(word)
            elif cur > 0 and cur + 1 + len(word) <= maxWidth:
                cur += 1 + len(word)
            else:
                res.append(self.fullJust(words[i:j], wordLen, maxWidth))
                i = j
                j -= 1
                cur = len(word)
                wordLen = 0
            wordLen += len(word)
        res.append(self.leftJust(words[i:len(words)], maxWidth))
        return res
                
                
    def leftJust(self, words, maxWidth):
        s = " ".join(words)
        if len(s) < maxWidth: s += " "*(maxWidth - len(s))
        return s        

    def fullJust(self, words, wordLen, maxWidth):
        s = words[0]
        totSpace = maxWidth - wordLen
        if len(words) > 1: 
            space = totSpace // (len(words) - 1)
            extra = totSpace - space*(len(words) - 1)     
        for i in range(1, len(words)):
            if extra > 0:
                s += " "*(space+1)
                totSpace -= space + 1
                extra -= 1
            else:
                s += " "*space
                totSpace  -= space
            s += words[i]
        s += " "*totSpace
        return s