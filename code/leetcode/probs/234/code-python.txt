# Reverse the first half and check node by node.
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        slow = fast = cur = head
        prev = None
        while fast and fast.next:
            cur = slow
            slow = slow.next
            fast = fast.next.next
            cur.next = prev
            prev = cur
            
        if fast and fast.next is None:
            slow = slow.next
            
        while cur and slow:
            if cur.val != slow.val:
                return False
            cur = cur.next
            slow = slow.next
        return True