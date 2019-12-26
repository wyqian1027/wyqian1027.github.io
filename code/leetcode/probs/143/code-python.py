class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head: return None
        
        fast = slow = head
        
        # find midpoint
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        mid = slow.next
        slow.next = None
        cur = mid
        pre = None
        p2 = None
        
        # reverse
        while cur:
            p2 = cur
            after = cur.next
            cur.next = pre
            pre = cur
            cur = after
        
        p1 = head
        # stitching
        while p1 and p2:
            p1after, p2after = p1.next, p2.next
            p1.next = p2
            p2.next = p1after
            p1, p2 = p1after, p2after
        
        return head