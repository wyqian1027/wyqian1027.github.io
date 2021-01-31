class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        def check(target, word):
            m, n = len(target), len(word)
            i = j = 0
            while i < m or j < n:
                if i >= m: return False
                if j >= n: return False
                ch_t, init_i = target[i], i
                ch_w, init_j = word[j], j
                if ch_t != ch_w: return False
                while i < m and target[i] == ch_t:
                    i += 1
                while j < n and word[j] == ch_w:
                    j += 1
                di, dj = i - init_i, j - init_j
                if di < dj: return False
                if di < 3 and di != dj: return False
            return True
        
        return sum(check(S, word) for word in words)
