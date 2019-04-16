class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        beginSt, endSt, wordSt = set(), set(), set(wordList)
        alphaSt = set('abcdefghijklmnopqrstuvwxyz')
        
        if endWord not in wordSt: return 0
        
        res = 1
        
        visitedSt = set()
        
        beginSt.add(beginWord)
        endSt.add(endWord)

        
        while beginSt and endSt:
            
            if len(beginSt) > len(endSt):
                beginSt, endSt = endSt, beginSt
            
            temp = set()
            
            for word in beginSt:
                word_list = list(word)
                for i in range(len(word_list)):
                    for ch in alphaSt:
                        
                        old = word_list[i]
                        word_list[i] = ch
                        target = "".join(word_list)
                        
                        if (target in endSt): return res + 1
                        
                        if (target not in visitedSt and target in wordSt):
                            temp.add(target)
                            visitedSt.add(target)
                        
                        word_list[i] = old
            
            beginSt = temp
            res += 1
        
        return 0
        