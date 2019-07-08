class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # BFS
        # q = collections.deque([self.root])
        # for ch in word:
        #     size = len(q)
        #     if size == 0: return False
        #     for _ in range(size):
        #         node = q.popleft()
        #         if ch == ".":
        #             for x in node.children:
        #                 q.append(node.children[x])
        #         elif ch in node.children:
        #             q.append(node.children[ch])
        # return any([x.end for x in q])
    
        # DFS
        def dfs(word, node):
            if not word:
                return node.end
            if node:
                ch, sub = word[0], word[1:]
                if ch == ".":
                    return any(dfs(sub, x) for x in node.children.values())
                else:
                    return dfs(sub, node.children[ch]) if ch in node.children else False
        node = self.root
        return dfs(word, node)