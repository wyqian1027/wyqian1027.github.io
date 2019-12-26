class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:

        counts = [0, 0]
        
        def count(node):
            L = R = 0
            if node.left: L = sum(count(node.left)) + 1
            if node.right: R = sum(count(node.right)) + 1
            if node.val == x:
                counts[0] = L
                counts[1] = R
            return (L, R)
            
        return sum(count(root)) // 2 < max(max(counts), n - sum(counts) - 1)    