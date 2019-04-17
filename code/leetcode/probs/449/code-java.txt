/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { 
 *         val = x; 
 *     }
 * }
 */
public class Codec {

    private static final String splitter = ",";
    private static final String NN = "null";
    
    public String serialize(TreeNode root) {

        StringBuilder sb = new StringBuilder();
        encode(sb, root);
        return sb.toString();
    }

    //preorder
    private void encode(StringBuilder sb, TreeNode root){
        if (root == null){
            sb.append(NN).append(splitter);
        } else {
            sb.append(String.valueOf(root.val)).append(splitter);
            encode(sb, root.left);
            encode(sb, root.right);
        }
    }

    public TreeNode deserialize(String data) {
        Queue<String> q = new LinkedList<>(Arrays.asList(data.split(splitter)));
        return decode(q);
    }

    private TreeNode decode(Queue<String> q) {
        String curr = q.poll();
        if (curr.equals(NN)) {
            return null;
        } else {
            TreeNode res = new TreeNode(Integer.parseInt(curr));
            res.left = decode(q);
            res.right = decode(q);
            return res;
        }
    }
}
