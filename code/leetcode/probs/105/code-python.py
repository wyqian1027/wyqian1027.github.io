class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
        
            root = TreeNode(preorder[0])
            
            ind = inorder.index(preorder[0])
            
            root.left = self.buildTree(preorder[1:1+ind], inorder[:ind])
            
            root.right = self.buildTree(preorder[1+ind:], inorder[ind+1:])
            
            return root
        
        return None

# Or using pop

def buildTree(self, preorder, inorder):

    if inorder:
    
        ind = inorder.index(preorder.pop(0))
        
        root = TreeNode(inorder[ind])
        
        root.left = self.buildTree(preorder, inorder[0:ind])
        
        root.right = self.buildTree(preorder, inorder[ind+1:])
        
        return root
        