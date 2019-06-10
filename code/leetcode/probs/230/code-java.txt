// 1. Recursion
class Solution {
    
    private TreeNode res;
    private int count = 0;
    public int kthSmallest(TreeNode root, int k) {
        visit(root, k);
        return res.val;
    }
    
    private void visit(TreeNode root, int k){
        if (root != null && this.count < k){
            visit(root.left, k);
            if (++this.count == k) res = root;
            visit(root.right, k);
        }
    }
}

// 2. Iterative
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        
        Stack<TreeNode> stack = new Stack<>();
        while (!stack.isEmpty() || root != null){
            if (root != null){
                stack.push(root);
                root= root.left;
            } else {
                root = stack.pop();
                if (--k == 0) return root.val;
                root = root.right;
            }
        }
        return -1;
    }
}