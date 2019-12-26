# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
from heapq import heappush, heappop

class Solution:
    def mergeKLists(self, lists):

        h = []
        c= 0
        for head in lists:
            if head:
                heappush(h, (head.val, c, head))   
                c += 1
        
        cur = dummy = ListNode(0)
        while h:
            val, _, node = heappop(h)
            cur.next = node
            cur = node
            
            c += 1
            if node.next:
                heappush(h, (node.next.val, c, node.next))
        
        return dummy.next