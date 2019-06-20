class Solution {
    public ListNode removeElements(ListNode head, int val) {
        
        ListNode dummy = new ListNode(val - 1);
        dummy.next = head;
        ListNode cur = dummy;
        
        while (head != null) {
            
            if (head.val == val){
                cur.next = head.next;
            } else {
                cur = cur.next;
            }
            
            head = head.next;
        }
        return dummy.next;
    }
}