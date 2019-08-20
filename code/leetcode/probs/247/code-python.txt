class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        d = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
                
        if n % 2 == 0:
            res = [""]
        else:
            res = ["0", "1", "8"]
        
        for i in range(n // 2):
            if i != n // 2 - 1:  
                res = [ k + el + v for el in res for k, v in d.items()]
            else:
                res = [ k + el + v for el in res for k, v in d.items() if k != "0"]
        
        return res