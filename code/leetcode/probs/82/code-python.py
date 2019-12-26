class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return head
        
        dummy = ListNode(head.val-1)
        dummy.next = head
        rollback = pre = last = dummy
        
        while head:

            if head.val == last.val:
                pre = rollback
                pre.next = None
            else:
                pre.next = head
                rollback = pre
                pre = pre.next
                
            last = head
            head = head.next
        
        return dummy.next