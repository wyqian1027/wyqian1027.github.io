class Solution {
    public int findNthDigit(int n) {
        
        long limit = 9;
        int digit = 1;
        
        // get digit
        while (n - limit*digit > 0){
            n -= limit*digit;
            digit++;
            limit *= 10;
        }
        
        // get number
        int x = 1;
        for (int i = 1; i < digit; i++) x *= 10;
        int index = n % digit;
        x += n / digit;
        if (index == 0) {
            x -= 1;       
            index = digit;
        }
        
        // while (m - digit > 0){
        //     x += 1;
        //     m -= digit;
        // }

        // get nth digit
        return Character.getNumericValue(Integer.toString(x).charAt(index - 1));
    }
}