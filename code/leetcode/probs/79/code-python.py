class Solution:
  
    def exist(self, board, word):
        
        if not word: return True
        numR, numC = len(board), len(board[0])
                
        def dfs(r, c, word, visited):
            
            if not word: return True
            
            for newR, newC in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if 0 <= newR < numR and 0 <= newC < numC and board[newR][newC] == word[0] and \
                (newR, newC) not in visited:
                    
                    visited.add((newR, newC))
                    
                    if dfs(newR, newC, word[1:], visited):
                        return True
                        
                    visited.remove((newR, newC))
            
            return False       
        
        for i in range(numR):
            for j in range(numC):
            
                if board[i][j] == word[0]:
                
                    if dfs(i, j, word[1:], set([(i,j)])):
                        return True
        
        return False