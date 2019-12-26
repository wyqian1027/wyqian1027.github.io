class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        Deque<TreeNode> queue = new ArrayDeque<>();
        List<List<Integer>> res = new LinkedList<List<Integer>>();
        if (root == null) return res;
        
        queue.offerLast(root);
        
        while (!queue.isEmpty()){
            
            List<Integer> level = new LinkedList<Integer>();
            int size = queue.size();
            
            for (int i = 0; i < size; i++){
                TreeNode cur = queue.pollFirst();
                level.add(cur.val);
                if (cur.left != null) queue.offerLast(cur.left);
                if (cur.right != null) queue.offerLast(cur.right);
            }
            
            res.add(level);         
        }  
        return res;       
    }
}