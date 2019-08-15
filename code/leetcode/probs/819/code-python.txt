# Using Replace 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banned = set(banned)
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        count = collections.Counter(word for word in paragraph.lower().split())
        ans, best = '', 0

        for word in count:
            if count[word] > best and word not in banned:
                ans = word
                best = count[word]
        return ans

# Character Traversal:
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banned = set(banned)
        punc = "!?',;. "
        count = Counter()
        cur = ""
        
        for ch in paragraph + " ":
            if ch not in punc:
                cur += ch
            elif cur:
                cur = cur.lower()
                if cur not in banned:
                    count[cur] += 1
                cur = ""
        return count.most_common(1)[0][0]