class Solution:

    # one scan
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        
        while n > 0:
            head = head.next
            n -= 1
        
        while head:
            cur = cur.next
            head = head.next
            
        cur.next = cur.next.next
        
        return dummy.next
        
    # first lengt, two scans
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        s = 0
        
        dummy = ListNode(0)
        dummy.next = head
        
        while head:
            head = head.next
            s += 1
        
        s -= n
        cur = dummy
        while cur and s > 0:
            cur = cur.next
            s -= 1
        
        cur.next = cur.next.next
        
        return dummy.next
        
        
        
        
        