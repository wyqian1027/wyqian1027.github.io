class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> arr = new LinkedList<Integer>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;
        
        while (cur != null || !stack.isEmpty()) {
            
            while (cur != null){
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            arr.add(cur.val);
            cur = cur.right;            
        }
        
        return arr;       
    }
}

// Alternatively:

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        
        List<Integer> arr = new LinkedList<Integer>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;
        
        while (cur != null || !stack.isEmpty()) {
            
            if (cur != null){
                stack.push(cur);
                cur = cur.left;
            } else {
                cur = stack.pop();
                arr.add(cur.val);
                cur = cur.right;   
            }
        }
        
        return arr;       
    }
}