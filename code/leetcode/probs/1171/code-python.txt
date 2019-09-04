class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        
        dh = ListNode(5000)
        dh.next = head
        
        d = collections.OrderedDict()
        prev, cur = dh, head
        acc = 0
        d[0] = dh
        
        while cur:
            acc += cur.val
            if acc not in d:
                d[acc] = cur
                cur = cur.next
            else:
                while acc in d:
                    k, last_seen = d.popitem()
                last_seen.next = cur.next
                d[acc] = last_seen
                cur = cur.next
        
        return dh.next