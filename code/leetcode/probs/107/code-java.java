//1. Iteration
class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        LinkedList<List<Integer>> res = new LinkedList<>();
        
        if (root == null) return res;
        
        queue.offer(root);
        while (!queue.isEmpty()){
            
            List<Integer> level = new ArrayList<>();
            int size = queue.size();
            
            while (size > 0) {
                TreeNode cur = queue.poll();
                level.add(cur.val);
                if (cur.left != null) queue.add(cur.left);
                if (cur.right != null) queue.add(cur.right);
                size--;
            }
            res.addFirst(level);
        }
        return res;
    }
}

//2. Recursion
class Solution {
    List<List<Integer>> res = new ArrayList<>();
    
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        dfs(root, 0);
        return res;        
    }
    
    private void dfs(TreeNode root, int depth){
        if (root == null) return;
        
        if (depth >= res.size()) {
            res.add(0, new ArrayList<Integer>());
        }
        res.get(res.size() - depth - 1).add(root.val);
        dfs(root.left, depth + 1);
        dfs(root.right, depth + 1);
    }
}