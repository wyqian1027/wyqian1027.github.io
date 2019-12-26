# Using bit array to label each word
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        if len(words) < 2: return 0
        maxLen = 0
        record = [0]*len(words)
        for i, word in enumerate(words):
            for ch in word:
                record[i] |= 1 << (ord(ch) - ord('a'))
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if record[i] & record[j] == 0:
                    maxLen = max(maxLen, len(words[i])* len(words[j]))
        return maxLen