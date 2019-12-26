class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.arr = []
        q = collections.deque([root])
        while q:
            x = q.popleft()
            self.arr.append(x)
            if x.left:  q.append(x.left)
            if x.right: q.append(x.right)    
        
    def insert(self, v: int) -> int:
        node = TreeNode(v)
        self.arr.append(node)
        n = len(self.arr)
        if n % 2 == 1:
            self.arr[n // 2 - 1].right = node
        else:
            self.arr[n // 2 - 1].left = node
        return self.arr[n // 2 - 1].val
        

    def get_root(self) -> TreeNode:
        return self.root