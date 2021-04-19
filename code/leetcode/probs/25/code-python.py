class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if k == 1: return head
        
        def is_k_nodes(head, k):
            while head and k > 0:
                head = head.next
                k -= 1
            return k == 0
        
        prev = dummy = ListNode(next=head)
        
        while is_k_nodes(head, k):
            # prev -> 1(p1) -> 2(p2) -> 3(p3) -> nxt group
            # prev ... 1 <- 2 <- 3 ... nxt group
            p1, p2, p3 = head, head.next, head.next.next
            for _ in range(k-1):
                p2.next = p1
                p1 = p2
                p2 = p3
                p3 = p3.next if p3 else None
            prev.next = p1
            head.next = p2
            prev = head
            head = p2
        
        return dummy.next
