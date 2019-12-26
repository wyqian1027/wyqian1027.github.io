class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new LinkedList<>();
        if (root == null) return res;
        dfs(root, "", res);
        return res;        
    }
    
    private void dfs(TreeNode root, String path, List<String> res){
        path += root.val;
        //leaf
        if (root.left == null && root.right == null){
            res.add(path);
            return;
        }
        // branch
        if (root.left != null) {
            dfs(root.left, path + "->", res);
        }
        if (root.right != null) {
            dfs(root.right, path + "->", res);
        }
    }
}