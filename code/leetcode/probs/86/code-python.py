class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = cur1 = ListNode()
        dummy2 = cur2 = ListNode()
        while head != None:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
            head = head.next
        cur1.next = dummy2.next
        cur2.next = None
        return dummy1.next
