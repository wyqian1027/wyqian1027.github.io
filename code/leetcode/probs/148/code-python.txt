class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head: return None
        if not head.next: return head
        
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        p1, p2 = head, slow.next
        slow.next = None
        
        p1 = self.sortList(p1)
        p2 = self.sortList(p2)
        return self.merge(p1, p2)       
        
    
    def merge(self, p1, p2):
        cur = dummy = ListNode(-1)
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        cur.next = p1 or p2
        return dummy.next