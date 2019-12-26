class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """

        # if cand exists, then we find it by chaining
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                cand = i
          
        # proof
        # does everyone know cand after cand?
        for i in range(cand, n):
            if not knows(i, cand):
                return -1
        
        # does everyone know cand before cand?
        for i in range(cand):
            if knows(cand, i):
                return -1
            if not knows(i, cand):
                return -1

        return cand