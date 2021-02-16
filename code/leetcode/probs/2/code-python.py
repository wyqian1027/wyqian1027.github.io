class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # I will add l2 to l1
        carry = 0
        dummy = cur = ListNode(-1)
        
        # add up the common length part
        while l1 and l2:
            val = l1.val + l2.val + carry
            cur.next = ListNode(val % 10)
            carry = val // 10
            l1 = l1.next
            l2 = l2.next
            cur = cur.next
        
        # take care of different part
        rem = l1 or l2
        while rem:
            val = rem.val + carry
            cur.next = ListNode(val % 10)
            carry = val // 10
            rem = rem.next
            cur = cur.next

            
        # take care of possible new digit
        if carry == 1: 
            cur.next = ListNode(1)
        
        return dummy.next

# alternatively
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = ListNode()
        cur = head
        c = 0
        
        while l1 or l2 or c != 0:
            s = c
            if l1: 
                s += l1.val
                l1 = l1.next
            if l2: 
                s += l2.val
                l2 = l2.next
            c = s // 10
            s = s % 10
            cur.next = ListNode(s)
            cur = cur.next
        
        return head.next
