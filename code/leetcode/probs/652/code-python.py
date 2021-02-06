# Both O(N) time, space complexity is reduced to O(N) since string concatenation is avoided.

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        count = collections.Counter()
        cache = {}
        ans = []
        def dfs(node):
            if not node: return "#"
            serial = "{},{},{}".format(node.val, dfs(node.left), dfs(node.right))
            count[serial] += 1
            if count[serial] == 2:
                ans.append(node)
            return serial
        dfs(root)
        return ans

    def findDuplicateSubtrees(self, root):
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__ # set a default value
        count = collections.Counter()
        ans = []
        def lookup(node):
            if node:
                # this line adds to dict AND returns the UID
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans