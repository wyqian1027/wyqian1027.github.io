class Solution:
    def findAllConcatenatedWordsInADict(self, words: 'List[str]') -> 'List[str]':

        st = set(words)
        memo = {}
        
        def dfs(word):
            if word in memo:
                return memo[word]
            
            memo[word] = False
            
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in st and suffix in st:
                    memo[word] = True
                    return True
                if prefix in st and dfs(suffix):
                    memo[word] = True
                    return True
                if suffix in st and dfs(prefix):
                    memo[word] = True
                    return True
            
            return memo[word]
        
        return [word for word in words if dfs(word)]