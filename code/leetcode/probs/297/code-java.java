public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        if (root == null) return "";
        StringBuilder sb = new StringBuilder();;
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        sb.append(Integer.toString(root.val));
        
        while (!queue.isEmpty()){
            TreeNode cur = queue.poll();
            if (cur.left != null) {
                queue.offer(cur.left);
                sb.append(",").append(Integer.toString(cur.left.val));
            } else {
                sb.append(",#");
            }
            if (cur.right != null) {
                queue.offer(cur.right);
                sb.append(",").append(Integer.toString(cur.right.val));
            } else {
                sb.append(",#");
            }
        }
        return sb.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String s) {
        if (s == null || s.length() == 0) return null;
        
        Queue<String> data = new LinkedList<>(Arrays.asList(s.split(",")));
        TreeNode root = new TreeNode(Integer.parseInt(data.poll()));
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        String val;
        
        while (!data.isEmpty()){
            TreeNode node = queue.poll();
            val = data.poll();
            if (val.equals("#")) {
                node.left = null;
            } else {
                node.left = new TreeNode(Integer.parseInt(val));
                queue.offer(node.left);
            }
            val = data.poll();
            if (val.equals("#")) {
                node.right = null;
            } else {
                node.right = new TreeNode(Integer.parseInt(val));
                queue.offer(node.right);
            }
        }
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));