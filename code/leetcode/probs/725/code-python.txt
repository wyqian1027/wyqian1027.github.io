class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        
        if not root: return [None]*k
        
        head = root
        length, i = [0]*k, 0
        
        while root:
            length[i] += 1
            root = root.next
            i = (i + 1) % k
        
        res = []
        for i in range(len(length)):
            if length[i] == 0:
                res.append(None)
            else:
                res.append(head)
                for _ in range(length[i]-1):
                    head = head.next
                nxt = head.next
                head.next = None
                head = nxt
        
        return res