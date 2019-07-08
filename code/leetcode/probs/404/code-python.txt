# Recursion without helper
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

# Recursion with helper
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.s = 0
        def visit(root, isLeft):
            if root:
                visit(root.left, True)
                if not root.left and not root.right and isLeft:
                    self.s += root.val
                visit(root.right, False)
        visit(root, False)
        return self.s