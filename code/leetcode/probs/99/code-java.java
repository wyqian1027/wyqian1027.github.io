// Inorder Traversal

class Solution {
    TreeNode first = null, second = null;
    TreeNode prev = new TreeNode(Integer.MIN_VALUE);
    
    public void recoverTree(TreeNode root) {        
        inorder(root);
        swap(first, second);
    }
    
    private void swap(TreeNode t1, TreeNode t2){
        int tmp = t1.val;
        t1.val = t2.val;
        t2.val = tmp;
    }
    
    private void inorder(TreeNode root){
        
        if (root == null) return;
        
        inorder(root.left);
        
        if (prev.val > root.val && first == null) {
            // System.out.println("Editted first to be " + prev.val);
            first = prev;
        }
        
        if (prev.val > root.val && first != null) {
            // System.out.println("Editted second to be " + root.val);
            second = root;
        }     
        prev = root;
        
        inorder(root.right);
    }
}