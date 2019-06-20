class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        smallCur = smallHead = None
        bigCur = bigHead = None
        cur = head
        
        while cur:
            if cur.val < x:
                if not smallHead:
                    smallCur = smallHead = cur
                else:
                    smallCur.next = cur
                    smallCur = cur
            else:
                if not bigHead:
                    bigCur = bigHead = cur
                else:
                    bigCur.next = cur
                    bigCur = cur
            cur = cur.next
        
        if not smallHead: return bigHead
        if not bigHead: return smallHead
        
        # must terminate properly!
        smallCur.next = bigHead
        bigCur.next = None
        return smallHead