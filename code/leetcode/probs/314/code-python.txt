# HashMap Level Order Traversal BFS

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root: return []
        cache = collections.defaultdict(list)
        minCol = 0
        maxCol = 0
        q = collections.deque([(root, 0)])
        
        while q:
            node, col = q.popleft()
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            cache[col].append(node.val)
            if node.left:
                q.append((node.left,  col-1))
            if node.right:
                q.append((node.right, col+1))

        res = []
        for x in range(minCol, maxCol+1):
            res.append(cache[x])
        return res