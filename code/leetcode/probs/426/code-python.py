# recursive solution:
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        def helper(root):
            """
            return the head of converted linkedlist
            """            
            node = Node(root.val)
            left_head = right_tail = node
            if root.left:
                left_head, left_tail = helper(root.left)
                node.left = left_tail
                left_tail.right = node
            if root.right:
                right_head, right_tail = helper(root.right)
                node.right = right_head
                right_head.left = node
            return left_head, right_tail
        
        if not root: return None
        head, tail = helper(root)
        head.left = tail
        tail.right = head
        return head