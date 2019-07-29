# Pass Prev Node as argument in DFS

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.longest = 1
        if not root: return 0
        self.dfs(root, None, 0)
        return self.longest

    def dfs(self, root, prev, pathLen):
        if prev and prev.val == root.val - 1:
            pathLen += 1
        else:
            pathLen = 1
        self.longest = max(self.longest, pathLen)
        if root.left:
            self.dfs(root.left, root, pathLen)
        if root.right:
            self.dfs(root.right, root, pathLen)