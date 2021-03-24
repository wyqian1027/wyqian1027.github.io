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

# with less pointers
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(-101, head)
        cur = head
        while cur:
            link = True
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                link = False
            if link: 
                prev.next = cur
                prev = cur
            cur = cur.next
        prev.next = None
        return dummy.next
