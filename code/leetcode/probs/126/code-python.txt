// Using Dict + List Comprehension
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        
        st = set(wordList)
        if endWord not in st: return []
        
        LETTERS = "abcdefghijklmnopqrstuvwxyz"
        layer = {}
        layer[beginWord] = [[beginWord]]
        res = []
        
        while layer:
            
            newLayer = collections.defaultdict(list)

            for curWord, path in layer.items():

                if curWord == endWord:
                    res += path
                else:        
                    for i in range(len(curWord)):
                        for ch in LETTERS:
                            mutatedWord = curWord[:i] + ch + curWord[i+1:]
                            if mutatedWord in st:
                                newLayer[mutatedWord] += [p + [mutatedWord] for p in path]
            if res: break                
            st -= set(newLayer.keys())
            layer = newLayer
        
        return res
        
//BFS single layer
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        res = []
        LETTERS = "abcdefghijklmnopqrstuvwxyz"
        st = set(wordList)
        if endWord not in st: return res
        
        q = collections.deque()
        q.append((beginWord, [beginWord]))
        
        while q:
            newSt = set()
            for _ in range(len(q)):
                cur, path = q.popleft()
                if cur == endWord: res.append(path)
                curList = list(cur)
                
                for i in range(len(curList)):
                    old = curList[i]
                    for ch in LETTERS:
                        curList[i] = ch
                        trans = "".join(curList)
                        if trans != cur and trans in st:
                            q.append((trans, path + [trans]))
                            newSt.add(trans)
                    curList[i] = old
                    
            if res: break
            st -= newSt
        
        return res