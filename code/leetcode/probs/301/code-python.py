# BFS, checking all substrings of length - 1
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        def is_valid(s):
            count = 0
            for ch in s:
                if ch == "(":
                    count += 1
                elif ch == ")":
                    count -= 1
                if count < 0: return False
            return count == 0
        
        q = collections.deque([s])
        res_visited = set()
        
        while q and len(res_visited) == 0 : # BFS for minimum removal
            
            visited = set()
            size = len(q)
            
            for _ in range(size):
                sub = q.popleft()
                if is_valid(sub) and sub not in res_visited:
                    res_visited.add(sub)
                    
                # if found, then no need to search in next layer
                if len(res_visited) == 0:
                    for i in range(len(sub)):
                        if sub[i] not in ["(", ")"]: continue
                        new_s = sub[:i] + sub[i+1:]
                        if new_s not in visited:
                            q.append(new_s)
                            visited.add(new_s)
                
        return list(res_visited)
                    