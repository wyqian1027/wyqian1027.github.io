class Solution:
    def findRedundantConnection(self, edges):

        p = list(range(1001))
        rnk = [0]*1001
        
        def find(x):
            if p[x] != x: p[x] = find(p[x])
            return p[x]
        
        for u, v in edges:
            ur, vr = find(u), find(v)
            if ur == vr:
                return [u, v]
            else:
                if rnk[ur] < rnk[vr]:
                    ur, vr = vr, ur
                p[vr] = ur
                if rnk[ur] == rnk[vr]:
                    rnk[ur] += 1