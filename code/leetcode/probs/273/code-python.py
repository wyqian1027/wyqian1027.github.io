class Solution:

    def numberToWords(self, n: int) -> str:
        
        TENS = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
        TEENS =["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", \
                "Eighteen", "Nineteen"]
        TYS  = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]    
        
        thousand= 1000
        million = 1000000
        billion = 1000000000
        
        if n == 0: 
            return "Zero"
        
        elif n <= 10:
            return TENS[n]
        
        elif n <= 19:
            return TEENS[n-10-1]
        
        elif n < 100:
            return TYS[n // 10 - 2] if n % 10 == 0 else \
                TYS[n // 10 - 2] + " " + self.numberToWords(n % 10)
        
        elif n < thousand:
            return TENS[n//100] + " Hundred" if n % 100 == 0 else \
                TENS[n//100] + " Hundred " + self.numberToWords(n % 100)
        
        elif n < million:
            return self.numberToWords(n // thousand) + " Thousand" if n % thousand == 0 else \
                self.numberToWords(n // thousand) + " Thousand " + self.numberToWords(n % thousand)
        
        elif n < billion:
            return self.numberToWords(n // million) + " Million" if n % million == 0 else \
                self.numberToWords(n // million) + " Million " + self.numberToWords(n % million)
        
        else:
            return self.numberToWords(n // billion) + " Billion" if n % billion == 0 else \
                self.numberToWords(n // billion) + " Billion " + self.numberToWords(n % billion)