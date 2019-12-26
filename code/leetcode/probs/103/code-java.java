class Solution {
    
    List<List<Integer>> res = new ArrayList<>();
    
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        boolean flip = false;
        
        if (root == null) return res;
        queue.offer(root);
        
        while(!queue.isEmpty()){
            
            int size = queue.size();
            List<Integer> level = new LinkedList<>();
            
            while (size > 0) {
                TreeNode cur = queue.poll();
                if (flip == false){
                    level.add(cur.val);
                } else {
                    level.add(0, cur.val);
                }
                if (cur.left != null) queue.offer(cur.left);
                if (cur.right != null) queue.offer(cur.right);
                size--;
            }
            res.add(level);            
            flip = (flip == false? true: false);   
        }
        return res;
    }
}