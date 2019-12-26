# Heap Solution:
from heapq import *
from collections import Counter
from collections import deque

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        d = Counter(s)
        h = []
        for ch, v in d.items():
            heappush(h, [-v, ch])
        
        store = deque([])
        res = []
        pos = 0
        
        while h:
            
            v, ch = heappop(h)
            res.append(ch)
            if v + 1 < 0:
                store.append([pos, v+1, ch])
            pos += 1
            
            if store and pos >= store[0][0] + k:
                _, v, ch = store.popleft()
                heappush(h, [v, ch])
            
        return "".join(res) if len(res) == len(s) else ""
        
# ARRAY SOLUTION:
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        
        valid = {ch: 0 for ch in set(s)}
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        
        # find element with most counts after index
        def helper(index):
            mostCount = 0
            el = ""
            for ch in count:
                if count[ch] > mostCount and index >= valid[ch]:
                    mostCount = count[ch]
                    el = ch
            return el
    
        ans = ""
        for i in range(len(s)):
            el = helper(i)
            if el == "": return ""
            ans += el
            count[el] -= 1
            valid[el] = i + k
        
        return ans