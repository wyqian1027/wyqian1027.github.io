class Solution:

    def oddEvenList(self, head):

        dummyOdd = ListNode(0)
        dummyEven = ListNode(0)
        odd = dummyOdd
        even = dummyEven
        i = 1
        
        while head:

            if i % 2 == 1:
                odd.next = head
                odd = head
            else:
                even.next = head
                even = head
            head = head.next
            i += 1
        
        odd.next = dummyEven.next
        even.next = None
        
        return dummyOdd.next