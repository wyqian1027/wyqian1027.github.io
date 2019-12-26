import random

class Solution:

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        count = 1
        cur = self.head
        while cur:
            if random.random() < 1/count:
                res = cur.val
            cur = cur.next
            count += 1
        return res