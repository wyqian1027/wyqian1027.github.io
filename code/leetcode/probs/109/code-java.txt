// 1. Best Solution Using Inorder Traversal. O(N) time, O(logN) space.
class Solution {
     
    private ListNode head;
    
    private int getSize(ListNode head){
        int size = 0;
        while (head != null) {
            head = head.next;
            size++;
        }
        return size;
    }
    
    public TreeNode sortedListToBST(ListNode head) {
        this.head = head;
        int size = getSize(head);
        return buildBST(0, size);
    }
    
    private TreeNode buildBST(int lo, int hi){
        
        if (lo >= hi) return null;
        
        int m = lo + (hi - lo) / 2;
        
        TreeNode left = buildBST(lo, m);
        TreeNode root = new TreeNode(head.val);
        head = head.next;
        TreeNode right = buildBST(m+1, hi);
        
        root.left = left;
        root.right = right;
        return root;
    }
}

// 2. Copy to Array then same as 108. O(N) time, O(N) space.