class Solution:

    def getIntersectionNode(self, h1, h2):
        
        cur1 = h1
        cur2 = h2
        
        while cur1 != cur2:
            
            cur1 = cur1.next if cur1 else h2
            cur2 = cur2.next if cur2 else h1
        
        return cur1

    # with flag
    def getIntersectionNode(self, h1, h2):

        cur1 = h1
        cur2 = h2
        check1 = True
        check2 = True
        
        while cur1 and cur2:
            
            if cur1 == cur2: return cur1
            
            cur1 = cur1.next
            cur2 = cur2.next
            
            if not cur1 and check1:
                cur1 = h2
                check1 = False
            
            if not cur2 and check2:
                cur2 = h1
                check2 = False
                
        return None