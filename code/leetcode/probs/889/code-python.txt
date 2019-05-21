class Solution:

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        if post:
            
            root = TreeNode(post.pop())
        
            if len(post) == 1: # deal with cases like [1, 2], [2, 1]
                root.left = TreeNode(post.pop())

            elif len(post) > 1:
                index = pre.index(post[-1])  # index of pre
                root.left = self.constructFromPrePost(pre[1:index], post[:index-1])
                root.right = self.constructFromPrePost(pre[index:], post[index-1:])

            return root
        
        return None