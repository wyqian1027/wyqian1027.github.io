class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        d = collections.defaultdict(list)
        for i in range(len(pid)):
            d[ppid[i]].append(pid[i])
        res = []
        q = [kill]
        while q:
            x = q.pop()
            res.append(x)
            q.extend(d[x])
        return res