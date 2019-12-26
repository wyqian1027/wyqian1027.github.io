class Solution:

    # iterative
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        
        while head and head.next:
            
            nxt = head.next.next
            pre.next = head.next
            head.next.next = head
            head.next = nxt
            pre = head
            head = nxt
            
        return dummy.next

    # recursive
    def swapPairs(self, head):
    
        if not head or not head.next: return head
        
        p = self.swapPairs(head.next.next)
        nxt = head.next
        nxt.next = head
        head.next = p
        return nxt