class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        size = 0
        cur = head
        while cur:
            size += 1
            cur = cur.next
        self.cur = head
        
        def helper(l, r):
            if l > r:
                return None
            mid = (l+r)//2
            
            left = helper(l, mid - 1)
            
            root = TreeNode(self.cur.val)
            root.left = left
            self.cur = self.cur.next
            
            root.right = helper(mid + 1, r)
            return root
        
        return helper(0, size-1)