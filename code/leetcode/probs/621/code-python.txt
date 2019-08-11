from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counts = Counter(tasks)
        total = len(tasks)
        valids = {k: 0 for k in counts}
        
        def helper(pos): # find the valid key with the largest count
            ans = "idle", 0
            for task in counts:
                if counts[task] > ans[1] and pos >= valids[task]:
                    ans = task, counts[task]
            return ans[0]
        
        pos = 0
        while total > 0:
            task = helper(pos)
            if task != "idle":
                total -= 1
                counts[task] -= 1
                if counts[task] == 0:
                    del counts[task]
                valids[task] = pos + n + 1
            pos += 1
        
        return pos