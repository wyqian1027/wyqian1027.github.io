// PriorityQueue Solution
class Solution {
        
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        
        List<Integer> ans = new ArrayList<>();
        PriorityQueue<TreeNode> queue = new PriorityQueue<TreeNode>(k, new Comparator<TreeNode>(){
            @Override
           public int compare(TreeNode n1, TreeNode n2) {
               double d1 = Math.abs(n1.val - target);
               double d2 = Math.abs(n2.val - target);
               if (d1 < d2) {
                   return -1;
               } else if (d1 == d2){
                   return 0;
               } else {
                   return 1;
               }
           }
        });
        inorder(root, queue);
        for (int i = 0; i < k; i++){
            ans.add(queue.poll().val);
        }
        return ans;
    }
    
    private void inorder(TreeNode root, PriorityQueue<TreeNode> queue){
        
        if (root != null) {
            inorder(root.left, queue);
            queue.add(root);
            inorder(root.right, queue);
        }
    }
}