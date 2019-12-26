class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        stack = []
        loc = 0
        ans = []
        
        while head:
            
            cur = head.val
            ans.append(0)
            while stack and stack[-1][0] < cur:
                _, idx = stack.pop()
                ans[idx] = cur
            stack.append((cur, loc))
            loc += 1
            head = head.next
        
        return ans