/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Codec {

    // Encodes an n-ary tree to a binary tree.
    public TreeNode encode(Node root) {
        if (root == null) return null;
        
        TreeNode treeRoot = new TreeNode(root.val);
                
        int size = root.children.size();
        
        if (size > 0) {
            treeRoot.left = encode(root.children.get(0));
        }
        
        TreeNode cur = treeRoot.left;
        
        for (int i = 1; i < size; i++){
            cur.right = encode(root.children.get(i));
            cur = cur.right;
        }
        return treeRoot;
    }

    // Decodes your binary tree to an n-ary tree.
    public Node decode(TreeNode treeRoot) {
        if (treeRoot == null) return null;
        
        Node root = new Node(treeRoot.val, new LinkedList<Node>());
        
        TreeNode cur = treeRoot.left;
        
        while (cur != null) {
            root.children.add(decode(cur));
            cur = cur.right;
        }
        
        return root;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(root));