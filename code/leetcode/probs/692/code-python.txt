from heapq import heappush, heappop

class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word
        
    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count
    
    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
    
    
class Solution:
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        ct = collections.Counter(words)
        
        h, res = [], []
        
        for word, count in ct.items():
            
            heappush(h, Element(count, word))
            
            if len(h) > k: heappop(h)
               
        for _ in range(k):
            
            res.append(heappop(h).word)
        
        return res[::-1]