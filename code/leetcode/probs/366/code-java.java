class Solution {
    
    List<List<Integer>> res = new ArrayList<>();
    
    public List<List<Integer>> findLeaves(TreeNode root) {
        
        getHeight(root);
        return res;
    }
    
    private int getHeight(TreeNode root) {
        
        if (root == null) return 0;
        int height = 1 + Math.max(getHeight(root.left), getHeight(root.right));
        while (res.size() < height) {
            res.add(new ArrayList<Integer>());
        }
        res.get(height-1).add(root.val);
        return height;       
    }
}