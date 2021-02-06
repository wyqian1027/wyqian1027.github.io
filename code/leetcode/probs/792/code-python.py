class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        
        # map first letter -> word (or iterator)
        candidates = collections.defaultdict(list)
        for word in words:
            it = iter(word)
            candidates[next(it)].append(it)
        
        # traverse the target string once
        count = 0
        for ch in S:
            pool = candidates[ch]
            candidates[ch] = []
            for it in pool:
                nxt = next(it, None)
                if nxt:
                    candidates[nxt].append(it)
                else:
                    count += 1
        return count
            