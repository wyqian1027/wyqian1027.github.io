/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        
        if (head == null) return null;
        
        int length = getLength(head);
        k = k % length;
        
        if (k == 0) return head;
        
        int index = 0;
        ListNode cur = head;
        while (index != length - k - 1) {
            index += 1;
            cur = cur.next;
        }
        
        ListNode ans = cur.next;
        cur.next = null;
        
        getLastNode(ans).next = head;
        
        return ans;
        
        
    }
    
    private int getLength(ListNode head) {
        int res = 0;
        while (head != null) {
            res += 1;
            head = head.next;
        }
        return res;
    }
    
    private ListNode getLastNode(ListNode head) {
        while (head.next != null) {
            head = head.next;
        }
        return head;
    }
}