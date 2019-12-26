// Iterative
class Solution {
    
    public ListNode reverseList(ListNode head) {
        
        ListNode pre = null;
        
        while (head != null){
            ListNode next = head.next;
            head.next = pre;
            pre = head;
            head = next;
        } 
        return pre;  
    }
}
    
// Recursive 1
class Solution {
    
    ListNode pre = null;
    
    public ListNode reverseList(ListNode head) {
        
        if (head == null) return pre;
        
        ListNode next = head.next;
        head.next = pre;
        pre = head;
        return reverseList(next);
    }
}

// Recursive 2
class Solution {
    
    public ListNode reverseList(ListNode head) {
        
        if (head == null || head.next == null) return head;
        
        ListNode p = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return p;        
    }
}