class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        
        #l2 by l1 2D dp memory
        #word2 is on vertical, word1 is on horizontal
        d = [[0]* (l1+1) for _ in range(l2+1)]         

        #init
        for i2 in range(1, l2+1):
            d[i2][0] = i2
        for i1 in range(1, l1+1):
            d[0][i1] = i1
        
        #compute
        for i in range(1, l2+1):
            for j in range(1, l1+1):
                if word2[i-1] == word1[j-1]:
                    d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1])
                else:
                    d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+1)
        
        return d[-1][-1]