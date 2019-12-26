from collections import deque

class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie.longest_word()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
    
    def longest_word(self):
        
        q = deque([(self.root, "")])
        ans = [""]
        
        while True:
            
            for i in range(len(q)):
                
                node, word = q.popleft()
                
                for c, nxt in node.children.items():

                    if nxt.end:
                        curWord = word + c
                        q.append((nxt, curWord))
            if not q: 
                break
            else:
                ans = [el[1] for el in q]
        
        return sorted(ans)[0]

        