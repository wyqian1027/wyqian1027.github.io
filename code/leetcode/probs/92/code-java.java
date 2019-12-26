class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;
        ListNode next = null;
        ListNode before = null;
        ListNode start = null;
        
        int i = 1;
        
        while (head != null) {
            
            if (i > n) break;
            
            next = head.next;
            
            if (i == m) {
                before = pre;
                start = head;
            }
            
            if (m <= i && i <= n) {
                head.next = pre;
            }
            
            pre = head;
            head = next;
            i++;
        }
        
        before.next = pre;
        start.next = head;
        return dummy.next;
    }
}