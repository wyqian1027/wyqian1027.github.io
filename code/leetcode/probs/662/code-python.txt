class Solution:

    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = collections.deque([(root, 0)])
        maxWidth = 0 

        while q:
            minLoc, maxLoc = float('inf'), -float('inf')
            size = len(q)
            for _ in range(size):
                node, loc = q.popleft()
                minLoc = min(minLoc, loc)
                maxLoc = max(maxLoc, loc)
                if node.left: q.append((node.left, 2*loc))
                if node.right: q.append((node.right, 2*loc+1))
            maxWidth = max(maxWidth, maxLoc-minLoc+1)
            
        return maxWidth

# Or just
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        q = collections.deque()
        q.append([root, 0])
        max_width = 1
        
        while q:
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            size = len(q)
            for _ in range(size):
                node, pos = q.popleft()
                if node.left:
                    q.append([node.left, pos*2])
                if node.right:
                    q.append([node.right, pos*2+1])                
        return max_width