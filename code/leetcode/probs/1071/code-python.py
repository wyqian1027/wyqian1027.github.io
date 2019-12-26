class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if len(str1) < len(str2):
            str1, str2 = str2, str1 # make str1 always longer  

        if len(str2) == 0: return str1
        
        if str1.startswith(str2):
            return self.gcdOfStrings(str2, str1[len(str2):])
        
        return ""