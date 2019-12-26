// similar idea, now with sorted set in the end to avoid duplicates

class Solution:
    def braceExpansionII(self, s: str) -> List[str]:
        
        groups = [[]]
        level = 0
        for i, c in enumerate(s):
            if c == '{':
                if level == 0:
                    start = i+1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.braceExpansionII(s[start: i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append([c])
                        
        st = set()
        for group in groups:
            st |= set(map(''.join, itertools.product(*group)))
        
        return sorted(st)