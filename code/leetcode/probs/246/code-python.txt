class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        d = {"6": "9", "9": "6", "1": "1", "0": "0", "8": "8"}
        
        i, j = 0, len(num) - 1
        
        while i <= j:
            if num[i] not in d or num[j] not in d:
                return False
            if d[num[i]] != num[j]:
                return False
            i += 1
            j -= 1
        
        return True