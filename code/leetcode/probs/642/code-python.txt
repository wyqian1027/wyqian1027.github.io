class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.data = None
        self.rank = 0
    
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        
        self.root = TrieNode()
        self.keyword = ""
        self.start = self.root
        for sen, time in zip(sentences, times):
            self.add_record(sen, time)
        
    def add_record(self, sen, time):
        cur = self.root
        for ch in sen:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.end = True
        cur.data = sen
        cur.rank -= time

    def search(self, keyword):
        cur = self.root
        for ch in keyword:
            if ch not in cur.children:
                return []
            cur = cur.children[ch]
        return self.search_from_node(cur)
    
    def search_from_node(self, node):
        res = []
        if node:
            if node.end:
                res.append((node.rank, node.data))
            for ch in node.children:
                res.extend(self.search_from_node(node.children[ch]))
        return res
        
    def input(self, c: str) -> List[str]:
        
        res = []
        if c != "#":
            self.keyword += c
            if c not in self.start.children:
                self.start = TrieNode()  # act like a stopper
            else:
                self.start = self.start.children[c]
                
            res = self.search_from_node(self.start)
        else:
            self.add_record(self.keyword, 1)
            self.keyword = ""
            self.start = self.root
        return [item[1] for item in sorted(res)[:3]]