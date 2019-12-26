class Solution1:
    def numComponents(self, head, G):
        st = set(G)
        cur = head
        ans = 0
        while cur:
            if (cur.val in st) and (cur.next ==  None or cur.next.val not in st):
                ans += 1
            cur = cur.next
        return ans   

class Solution2:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        
        p = list(range(10000))
        ranks = [0]*10000
        st = set(G)
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def merge(x, y):
            xr, yr = find(x), find(y)
            if x != y:
                if ranks[xr] < ranks[xr]:
                    xr, yr = yr, xr
                p[xr] = yr
                if ranks[xr] == ranks[yr]: ranks[xr] += 1
            
        while head and head.next:
            if head.val in st and head.next.val in st:
                merge(head.val, head.next.val)
            head = head.next
        
        return len(set(map(find, list(G))))