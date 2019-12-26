// Using Tree Traversal O(logN) space.

class BSTIterator {

    private Stack<TreeNode> stack;
    
    private void getLeftMostNode(TreeNode root) {
        while (root != null){
            stack.push(root);
            root = root.left;
        }
    }
    
    public BSTIterator(TreeNode root) {
        stack = new Stack<TreeNode>();
        getLeftMostNode(root);
    }
    
    /** @return the next smallest number */
    public int next() {
        TreeNode root = stack.pop();
        if (root.right != null){
            getLeftMostNode(root.right);
        }
        return root.val;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return stack.size() > 0;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
 
 // Alternatively, one can first copy the entire tree. O(N) space.