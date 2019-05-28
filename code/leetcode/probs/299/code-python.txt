class Solution:
    
    def getHint(self, secret: str, guess: str) -> str:
    
        ct = collections.Counter(secret)
        ct2= collections.Counter(guess)
        
        x = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1

        y = sum((ct & ct2).values()) - x
                        
        return "{}A{}B".format(x, y)