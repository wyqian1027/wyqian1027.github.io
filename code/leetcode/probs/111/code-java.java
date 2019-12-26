class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        
        if (root.left == null && root.right == null) return 1;
        
        int val = Integer.MAX_VALUE;
        
        if (root.left != null) val = Math.min(val, minDepth(root.left));
        if (root.right != null) val = Math.min(val, minDepth(root.right));
        
        return 1 + val;
    }
}

class Solution {
    public int minDepth(TreeNode root) {
        
        if (root == null) return 0;
        
        Queue<TreeNode> queue = new LinkedList<>();
        int level = 1;
        queue.offer(root);
        
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++){
                TreeNode cur = queue.poll();
                if (cur.left == null && cur.right == null) return level;
                if (cur.left != null) queue.offer(cur.left);
                if (cur.right != null) queue.offer(cur.right);
            }
            level += 1;                        
        }
        return level;        
    }
}