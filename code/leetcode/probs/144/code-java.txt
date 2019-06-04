//1. Using Stack to Store essentially the right children.

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        
        LinkedList<Integer> arr = new LinkedList<>();
        Stack<TreeNode> stack = new Stack<>();
        if (root == null) return arr;
        stack.push(root);
        
        while (!stack.isEmpty()){
            TreeNode cur = stack.pop();
            arr.add(cur.val);
            if (cur.right != null) stack.push(cur.right);
            if (cur.left != null) stack.push(cur.left);
        }
        
        return arr;       
    }
}

//2. General Approach with additional pointer.

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        
        LinkedList<Integer> arr = new LinkedList<>();
        Stack<TreeNode> stack = new Stack<>();
        if (root == null) return arr;
        TreeNode cur = root;
        
        while (cur != null || !stack.isEmpty()){
            
            while (cur != null){
                stack.push(cur);
                arr.add(cur.val);
                cur = cur.left;
            }
            cur = stack.pop();
            cur = cur.right;
        }
        
        return arr;       
    }
}