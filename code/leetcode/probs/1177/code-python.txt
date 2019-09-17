class Solution:

    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnt = [[0] * 26]
        for i, c in enumerate(s):
            cnt.append(cnt[i][:])
            cnt[i + 1][ord(c) - ord('a')] += 1
        return [sum((cnt[hi + 1][i] - cnt[lo][i]) % 2 for i in range(26)) // 2 <= k for lo, hi, k in queries]
                    