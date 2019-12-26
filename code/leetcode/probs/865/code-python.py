# 1. Get Depths and Parents, then find parents

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        parents = {}
        depths = collections.defaultdict(list)
        
        def get_depth(root, depth, parent):
            if root:
                depths[depth].append(root)
                parents[root] = parent
                get_depth(root.left, depth + 1, root)
                get_depth(root.right, depth + 1, root)
        
        get_depth(root, 0, None)
        deepest = depths[max(depths.keys())]
        
        if len(deepest) == 1: return deepest[0]
           
        while len(deepest) > 1:
            deepest = set([parents[x] for x in deepest])
            
        return deepest.pop()
        
# 2. Use Recursion
class Solution:

    def dfs(root):
        if not root: return (None, 0)
        L, R = dfs(root.left), dfs(root.right)
        if L[1] > R[1]: return (L[0], L[1]+1)
        if L[1] < R[1]: return (R[0], R[1]+1)
        return (root, L[1]+1)

    return dfs(root)[0]