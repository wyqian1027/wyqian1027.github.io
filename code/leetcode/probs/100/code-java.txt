// 1. Iteration: O(N) time O(N) space (worst)
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        
        if (p == null && q == null) return true;
        if (!check(p, q)) return false;
        
        Deque<TreeNode> queue1 = new ArrayDeque<>();
        Deque<TreeNode> queue2 = new ArrayDeque<>();
        queue1.offerLast(p);
        queue2.offerLast(q);
        
        while (!queue1.isEmpty() && !queue2.isEmpty()) {
            TreeNode t1 = queue1.pollFirst();
            TreeNode t2 = queue2.pollFirst();
            if (!check(t1, t2)) {
                return false;
            }
            if (t1 != null && t2 != null){
                if (!check(t1.left, t2.left)) return false;
                if (t1.left != null) {
                    queue1.offerLast(t1.left);
                    queue2.offerLast(t2.left);
                }
                if (!check(t1.right, t2.right)) return false;
                if (t1.right != null) {
                    queue1.offerLast(t1.right);
                    queue2.offerLast(t2.right);
                }
            }
        }
        
        return true;        
    }
    
    public boolean check(TreeNode p, TreeNode q){
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        return p.val == q.val;
    }
}

// 2. Recusion: (same)
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p != null && q != null && p.val == q.val){
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);    
        } else {
            return false;
        }
    }
}