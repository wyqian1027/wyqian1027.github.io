class Solution:

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return head
        dummy = head
        
        while head:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return dummy
    
    
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head or not head.next: return head
        dummy = ListNode(head.val - 1)
        dummy.next = head
        pre = dummy
        
        while head:
            if head.val != pre.val:
                pre.next = head
                pre = head               
            head = head.next
        
        pre.next = None
        return dummy.next