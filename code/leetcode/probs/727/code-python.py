class Solution:
    def minWindow(self, S: str, T: str) -> str:
        
        ans = [None, None, float('inf')]
        
        i = 0
        while i < len(S):
            if S[i] == T[0]:
                index_S = i
                index_T = 0
                found = False
                while index_S < len(S):
                    if S[index_S] == T[index_T]:
                        index_T += 1
                    index_S += 1
                    if index_T >= len(T):
                        found = True
                        break
                if found:
                    right = index_S
                    index_T = len(T) - 1
                    index_S -= 1
                    while index_S >= 0:
                        if S[index_S] == T[index_T]:
                            index_T -= 1
                        index_S -= 1
                        if index_T < 0:
                            break
                    left = index_S + 1
                    if right - left < ans[2]:
                        ans = left, right, right - left
                i = index_S + 2
            else:
                i += 1
        return S[ans[0]:ans[1]] if ans[2] != float('inf') else ""