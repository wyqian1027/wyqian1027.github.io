// 1. Using level and itertools.product
class Solution:
    def expand(self, s: str) -> List[str]:
        
        groups = [[]]
        level = 0
        
        for i, c in enumerate(s):
            
            if c == '{':
                if level == 0:
                    start = i + 1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    groups[-1].append(self.expand(s[start: i]))
            elif c == ',' and level == 0:
                groups.append([])
            elif level == 0:
                groups[-1].append(c)
            
        st = set()
        
        for group in groups:
            st |= set(map("".join, itertools.product(*group)))
            
        return sorted(st)
    
// 2. Shorter way
class Solution
    def expand(self, s):
        
        A = s.replace("{", " ").replace("}", " ").split(" ")
        B = [x.split(",") for x in A]
        return sorted(set(map("".join, itertools.product(*B))))