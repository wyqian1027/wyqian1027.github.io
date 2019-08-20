# 1. Binary Search O(NlogN) time, O(N) space
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        num_subs = 0
        
        source_dict = collections.defaultdict(list)
        for i, ch in enumerate(source):
            source_dict[ch].append(i)
            
        loc = 0 
        for ch in target:
            if ch not in source_dict: return -1
            
            j = bisect.bisect_left(source_dict[ch], loc)
            if j == len(source_dict[ch]):
                j = 0
                num_subs += 1
            
            loc = source_dict[ch][j] + 1
        
        return num_subs + 1

# 2. Two Pointer BruteForce O(N^2) time, O(1) space        
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        
        num_subs = 0
        
        ns, nt = len(source), len(target)
        start_loc = {}
        for i, ch in enumerate(source):
            if ch in start_loc: continue
            start_loc[ch] = i
        for ch in target:
            if ch not in start_loc: return -1
            
        i = 0
        while i < nt:
            num_subs += 1
            start = start_loc[target[i]]
            for j in range(start, ns):
                if i >= nt: break
                if source[j] == target[i]:
                    i += 1

        return num_subs