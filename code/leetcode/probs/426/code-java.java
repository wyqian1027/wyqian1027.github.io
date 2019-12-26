class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

class Solution {
    
    private Node first = null;
    private Node prev = null;
    
    public Node treeToDoublyList(Node root) {
        
        if (root == null) return null;
        traverse(root);
        first.left = prev;
        prev.right = first;
        return first; 
    }
    
    private void traverse(Node root){
        
        if (root != null){
            
            traverse(root.left);
            
            if (first == null) {
                first = root;
            } else {
                prev.right = root;
                root.left = prev;
            }
            prev = root;
            traverse(root.right);
        }
    }
}