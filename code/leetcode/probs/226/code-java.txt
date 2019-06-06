class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null) return root;
        TreeNode leftSub = root.left;
        TreeNode rightSub = root.right;
        root.left = invertTree(rightSub);
        root.right = invertTree(leftSub);
        return root;
    }
}