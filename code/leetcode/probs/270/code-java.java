// Recursive
class Solution {
    public int closestValue(TreeNode root, double target) {

        return visit(root, target, root.val);
    }
    
    private int visit(TreeNode root, double target, int val){
        if (root == null) return val;
        if (Math.abs(target - root.val) < Math.abs(target - val)){
            val = root.val;
        }
        if (root.val < target) {
            val = visit(root.right, target, val);
        } else {
            val = visit(root.left, target, val);
        }
        return val;
    }
}