# without using reverse:
class Solution:

    def plusOne(self, head: ListNode) -> ListNode:
        
        start = None
        cur = head
        
        while cur:
            if cur.val < 9:
                start = cur
            cur = cur.next
        
        if start:
            start.val += 1
            cur = start.next
        else:
            newH = ListNode(1)
            newH.next = head
            head = newH
            cur = head.next
        
        while cur:
            cur.val = 0
            cur = cur.next
            
        return head

# reverse, add one, reverse
class Solution:

    def plusOne(self, head: ListNode) -> ListNode:
        
        cur = root = self.reverse(head)
        
        carry = 1
        while cur:
            if cur.val + carry > 9:
                cur.val = 0
                carry = 1
            else:
                cur.val += carry
                carry = 0
                break
            cur = cur.next
        
        if carry == 0:
            return self.reverse(root)
        else:
            nxt = self.reverse(root)
            ans = ListNode(1)
            ans.next = nxt
            return ans
 
    def reverse(self, head):
        
        if not head or not head.next: return head
        
        p = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return p