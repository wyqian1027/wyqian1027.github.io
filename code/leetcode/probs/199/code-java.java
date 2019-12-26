class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        
        if (root == null) return res;
        
        q.add(root);
        while (!q.isEmpty()){
            int size = q.size();
            TreeNode cur = null;
            while (size > 0 ){
                cur = q.poll();
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
                size--;
            }
            if (cur != null) res.add(cur.val);            
        }
        return res;
    }
}