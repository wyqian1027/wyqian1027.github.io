class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
            
        dummy = ListNode(next=head)
        node = head
        
        while node and node.next:
            # using the invariants that previous list is sorted!
            if node.val <= node.next.val:
                node = node.next
            else:
                insert_node = node.next
                node.next = node.next.next
                cur = dummy
                # using "cur.next", instead of an extra "pre" cursor
                while cur.next.val <= insert_node.val:
                    cur = cur.next
                insert_node.next = cur.next
                cur.next = insert_node

        return dummy.next