# Mathematically find locations

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        
        d = {}
        q = collections.deque([(root, 0, 0)]) # node, row num, col num
        h = 0
        
        while q:
            node, row, col = q.popleft()
            d[node] = (row, col)
            h = max(h, row)
            if node.left: q.append((node.left,  row+1, 2*col))
            if node.right: q.append((node.right, row+1, 2*col+1))
            
        res = [[""]*(2**(h+1)-1) for _ in range(h+1)]
        
        for node in d:
            r, c = d[node]
            index = shift = 2**(h - r) - 1
            delta = 2**(h - r + 1)
            while c != 0:
                index += delta
                c -= 1
            res[r][index] = str(node.val)
        
        return res

# Using ideas from binary search

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        
        def get_max_height(root):
            if not root: return 0
            return 1 + max(get_max_height(root.left), get_max_height(root.right))
        
        h = get_max_height(root)
        
        res = [[""]*(2**h-1) for _ in range(h)]
        
        def fill_res(root, row, left, right):
            if root:
                m = (left + right) // 2
                res[row][m] = str(root.val)
                fill_res(root.left,  row + 1, left, (left + right) // 2 - 1 )
                fill_res(root.right, row + 1, (left + right) // 2 + 1, right)
        
        fill_res(root, 0, 0, len(res[0]) - 1)
        
        return res