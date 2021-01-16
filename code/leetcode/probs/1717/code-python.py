class Solution:
    def maximumGain_dp(self, s: str, x: int, y: int) -> int:
        
        # time overflow
        cache = {}
        def calc(s):
            if len(s) < 2: return 0
            if s in cache: return cache[s]
            maxScore = 0
            for i in range(len(s)-1):
                if s[i:i+2] == "ab":
                    maxScore = max(maxScore, calc(s[:i] + s[i+2:]) + x)
                if s[i:i+2] == "ba":
                    maxScore = max(maxScore, calc(s[:i] + s[i+2:]) + y)
            cache[s] = maxScore
            return maxScore
        start = 0
        total = 0
        for i in range(len(s)):
            if s[i] != "a" and s[i] != "b":
                total += calc(s[start:i]) if start < i else 0
                start = i + 1
        return total + calc(s[start:len(s)])

    def maximumGain(self, s: str, x: int, y: int) -> int:
        a = 'a'
        b = 'b'
        if x < y:
            x, y = y, x
            a, b = b, a
        
        # now ba is always worth more
        # use ba first then ab    
        score = 0
        count = {a:0, b:0}
        for i, char in enumerate(s):
            if char == a:
                count[a] += 1
            elif char == b:
                if count[a] >= 1:
                    count[a] -= 1
                    score += x
                else:
                    count[b] += 1
            else:
                score += min(count[a], count[b]) * y
                count[a] = count[b] = 0

        score += min(count[a], count[b]) * y

        return score