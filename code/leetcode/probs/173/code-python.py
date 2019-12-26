class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.cur = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.stack or self.cur:
            while self.cur:
                self.stack.append(self.cur)
                self.cur = self.cur.left
            self.cur = self.stack.pop()
            ans = self.cur.val
            self.cur = self.cur.right
            return ans

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.cur or self.stack