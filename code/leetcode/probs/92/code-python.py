class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right: return head
        dummy = ListNode(next=head)     
        c = 1
        prev = dummy
        before = None

        while head != None and c <= right:
            nxt = head.next
            if c == left:
                before = prev
            elif left < c <= right:
                head.next = prev
            c += 1
            prev = head
            head = nxt

        before.next.next = head
        before.next = prev

        return dummy.next
