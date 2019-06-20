class Solution:
    def hasCycle(self, head):

        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        
        return False