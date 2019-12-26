// two solutions:
class Solution {
    
    private TreeNode ans = null;
    
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (root == null) return ans;
        
        if (root.val > p.val) {
            ans = root;
            return inorderSuccessor(root.left, p);
        }
        else {
            return inorderSuccessor(root.right, p);
        }
    }
}

class Solution {

    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        TreeNode ans = null;
        while (root != null) {
            if (root.val > p.val){
                ans = root;
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return ans;
    }
}