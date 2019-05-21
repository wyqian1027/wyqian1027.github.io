class Solution {

    public boolean isSubtree(TreeNode s, TreeNode t) {
     
        if (s == null) {
            return (t == null ? true : false);
        }
        
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = s;
        
        while (cur != null || stack.size() > 0) {
            
            while (cur != null) {
                
                stack.push(cur);
                cur = cur.left;
            }
            
            cur = stack.pop();
            
            if (isSameTree(cur, t)) return true;
            
            cur = cur.right;
        }
        
        return false;
 
     }
    
    private boolean isSameTree(TreeNode s, TreeNode t) {
        
        if (s == null && t == null) {
            
            return true;
            
        } else if (s != null && t != null && s.val == t.val) {
            
            return isSameTree(s.left, t.left) && isSameTree(s.right, t.right);
            
        } else {
            
            return false;
            
        }
    }
}