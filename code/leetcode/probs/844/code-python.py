class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        i = len(S) - 1
        j = len(T) - 1
        
        while True:
            count_s, count_t = 0, 0
            while i >= 0 and (S[i] == "#" or count_s > 0):
                if S[i] == "#": 
                    count_s += 1
                else:
                    count_s -= 1
                i -= 1
            while j >= 0 and (T[j] == "#" or count_t > 0):
                if T[j] == "#": 
                    count_t += 1
                else:
                    count_t -= 1
                j -= 1
            # print("checking ", i, j)
            if i >= 0 and j >= 0:
                if S[i] != T[j]: 
                    return False
                else:
                    i -= 1
                    j -= 1
            elif i < 0 and j < 0:
                return True
            else:
                return False