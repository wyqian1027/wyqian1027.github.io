class Solution {
    
    String[] digit = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    String[] firstTen = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    String[] tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    
    int billion = 1000000000;
    int million = 1000000;
    int thousand = 1000;
    
    public String numberToWords(int num) {
        
        if (num >= billion){
            
            return (num % billion > 0 ? numberToWords(num / billion) + " Billion " + numberToWords(num % billion) : 
                    numberToWords(num / billion) + " Billion");
            
        } else if (num >= million && num < billion) {
            
            return (num % million > 0 ? numberToWords(num / million) + " Million " + numberToWords(num % million) :
                    numberToWords(num / million) + " Million");
            
        } else if (num >= thousand && num < million) {
            
            return (num % thousand > 0 ? numberToWords(num / thousand) + " Thousand " + numberToWords(num % thousand) :
                    numberToWords(num / thousand) + " Thousand");
            
        } else if (num >= 100 && num < thousand) {
            
            return (num % 100 > 0 ? numberToWords(num / 100) + " Hundred " + numberToWords(num % 100) : 
                    numberToWords(num / 100) + " Hundred");
            
        } else if (num >= 20 && num < 100){
            
            return (num % 10 > 0 ? tens[num / 10] + " " + digit[num % 10] : tens[num / 10]);
            
        } else if (num >= 10 && num < 20){
            
            return firstTen[num % 10];
            
        } else {
            
            return digit[num];
        }
    }
    
}