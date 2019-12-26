class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        a1, a2 = self.getList(l1), self.getList(l2)
        res = []
        carry = 0
        head = None
        
        while a1 or a2 or carry:
            val = carry
            if a1: val += a1.pop()
            if a2: val += a2.pop()
            res.append(val % 10)
            carry = val // 10
            cur = ListNode(val % 10)
            cur.next = head
            head = cur
        
        return head

    def getList(self, l1):
        res = []
        while l1:
            res.append(l1.val)
            l1 = l1.next
        return res