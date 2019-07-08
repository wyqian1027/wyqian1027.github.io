class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            cur = root
            for ch in word:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            cur.end = True
        
        self.res = set()
        used = [[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, "", i, j, root, used)
        return list(self.res)

    def dfs(self, board, word, i, j, cur, used):
        if cur.end:
            self.res.add(word)
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return
        ch = board[i][j]
        if not used[i][j] and ch in cur.children:
            used[i][j] = True
            self.dfs(board, word + ch, i+1, j, cur.children[ch], used)
            self.dfs(board, word + ch, i-1, j, cur.children[ch], used)
            self.dfs(board, word + ch, i, j+1, cur.children[ch], used)
            self.dfs(board, word + ch, i, j-1, cur.children[ch], used)
            used[i][j] = False        