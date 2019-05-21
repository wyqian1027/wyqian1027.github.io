// 1. Recursion
class Solution {
    
    int total = 0;
    
    public int findTilt(TreeNode root) {
        
        traverseTilt(root);
        return total;   
    }
    
    public int traverseTilt(TreeNode root) {
        if (root == null) return 0;
        
        int left = traverseTilt(root.left);
        int right = traverseTilt(root.right);
        total += Math.abs(left - right);
        return left + right + root.val;
    }
    
}

// 2. With Map

class Solution {
    
    Map<TreeNode, Integer> cache = new HashMap<>();
    int total = 0;
    
    public int findTilt(TreeNode root) {
        
        traverseTilt(root);
        
        return total;   
    }
    
    public void traverseTilt(TreeNode root) {
        if (root == null) return;
        
        total += Math.abs(sumNode(root.left) - sumNode(root.right));
        
        traverseTilt(root.left);
        traverseTilt(root.right);
    }
    
    
    public int sumNode(TreeNode root) {
        
        if (root == null) return 0;
        
        int res;
        if (cache.containsKey(root)) {
            res = cache.get(root);
        } else {
            res = root.val + sumNode(root.left) + sumNode(root.right);
            cache.put(root, res);
        }
        return res;       
    }
}