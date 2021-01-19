class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        dp = {}
        
        words.sort(key=len)
        for word in words:
            dp[word] = max(1 + dp.get(word[:i] + word[i+1:], 0) for i in range(len(word)))
        return max(dp.values())
            