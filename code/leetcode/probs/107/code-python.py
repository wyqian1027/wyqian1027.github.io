class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        q = collections.deque([(root, 0)])
        
        while q:
            node, depth = q.popleft()
            if len(res) <= depth:
                res.append([node.val])
            else:
                res[depth].append(node.val)
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        
        return res[::-1]

// Python List Comprehension
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        
        level = [root]
        res = []
        
        while root and level:
            res.append([node.val for node in level])    
            pairs = [(node.left, node.right) for node in level]
            level = [node for pair in pairs for node in pair if node != None]
        return res[::-1]