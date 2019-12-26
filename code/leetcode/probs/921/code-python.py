class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        
        balance = needed = 0
        
        for ch in S:
            if ch == "(":
                balance += 1
            elif ch == ")":
                balance -= 1
            if balance < 0:  # only way to make this valid is to add "(" on the left
                needed += 1
                balance = 0
        
        return balance + needed