class Solution:
    
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        
        dummy = ListNode(val-1)
        dummy.next = head
        cur = dummy
        
        while head:
            
            if head.val == val:
                cur.next = head.next
            else:
                cur = cur.next
            
            head = head.next
            
        return dummy.next