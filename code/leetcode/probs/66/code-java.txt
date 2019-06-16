class Solution {
    public int[] plusOne(int[] digits) {
        
        int carry  = 1;
        for (int i = digits.length - 1; i >= 0; i--){
            if (carry == 1 && digits[i] == 9) {
                digits[i] = 0;
                carry = 1;
            } else if (carry == 1) {
                digits[i] += 1;
                carry = 0;
            } else {
                break;
            }
        }
        
        if (carry == 1) {
            int[] newDigits = new int[digits.length + 1];
            newDigits[0] = 1;
            return newDigits;
        }
        return digits;
    }
}