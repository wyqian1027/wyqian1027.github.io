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

# Better Design as follows
class WordDictionary:

    def __init__(self):
        self.root = {}
        
    def addWord(self, word: str) -> None:
        cur = self.root
        for ch in word:
            if ch not in cur: cur[ch] = {}
            cur = cur[ch]
        cur["#"] = "#"
    
    def search_from_node(self, word, node):
        if not word: return "#" in node
        first = word[0]
        if first == ".":
            for ch in node:
                if ch != "#" and self.search_from_node(word[1:], node[ch]):
                    return True
            return False
        else:
            return self.search_from_node(word[1:], node[first]) if first in node else False          

    def search(self, word: str) -> bool:
        return self.search_from_node(word, self.root)