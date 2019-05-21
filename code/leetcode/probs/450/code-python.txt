class Solution:
    
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key > root.val:
        
            root.right = self.deleteNode(root.right, key)
            
        elif key < root.val:
        
            root.left = self.deleteNode(root.left, key)

        else:
            if not (root.left or root.right):
                root = None
                
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)

            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
                        
        return root
        
    # these give None if no successor/predecessor exists
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
            
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
            
        return root.val        
        
        
        