class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        
        if len(words1) != len(words2): return False
        
        parents = {}
        ranks = {}
        
        def makeset(word):
            if word not in parents:
                parents[word] = word
                ranks[word] = 0
        
        def find(word):
            if parents[word] != word:
                parents[word] = find(parents[word])
            return parents[word]
        
        def union(word1, word2):
            p1, p2 = find(word1), find(word2)
            if p1 == p2:
                return False
            else:
                if ranks[p1] < ranks[p2]:
                    p1, p2 = p2, p1
                parents[p2] = p1
                if ranks[p1] == ranks[p2]:
                    ranks[p1] += 1
                return True
        
        for u, v in pairs:
            makeset(u)
            makeset(v)
            union(u, v)
            
        for w1, w2 in zip(words1, words2):
            makeset(w1)
            makeset(w2)
            if find(w1) != find(w2):
                return False
        
        return True