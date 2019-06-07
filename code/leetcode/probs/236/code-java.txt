//1. Recursion
class Solution {
    
    TreeNode ans = null;
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        visit(root, p, q);
        return ans;
    }
    
    private boolean visit(TreeNode root, TreeNode p, TreeNode q){
        if (root == null) return false;
        
        int L = visit(root.left, p, q) ? 1 : 0;
        int R = visit(root.right, p, q) ? 1 : 0;
        int M = (root == p || root == q) ? 1 : 0;
        
        if (L + R + M >= 2) ans = root;
        
        return (L + R + M > 0);        
    }
}

// 2. Building Parent Dict First then check intersection
class Solution {
    Map<TreeNode, TreeNode> map = new HashMap<>();
    
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        Queue<TreeNode> queue = new LinkedList<>();
        if (root == null) return null;
        
        queue.offer(root);
        map.put(root, null);
        
        while (!(map.containsKey(p) && map.containsKey(q))) {
            TreeNode cur = queue.poll();
            if (cur.left != null) {
                queue.offer(cur.left);
                map.put(cur.left, cur);
            }
            if (cur.right != null) {
                queue.offer(cur.right);
                map.put(cur.right, cur);
            }
        }
        
        Set<TreeNode> set = new HashSet<>();
        while (p != null){
            set.add(p);
            p = map.get(p);
        }
        while (!set.contains(q)){
            q = map.get(q);
        }
        
        return q;
    }
}