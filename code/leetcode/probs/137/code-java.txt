class Solution {
    // Building a k-counter
    public int singleNumber(int[] nums) {
        int[] bitCount = new int[32];
        int k = 3;
        
        for (int n : nums) {
            for (int i = 0; i < 32; i++) {
                boolean hasBit = (n & (1 << i)) != 0;
                if (hasBit) {
                    bitCount[i] = (bitCount[i] + 1) % k;
                }
            }
        }
        
        int exept = 0;
        for (int i = 0; i < 32; i++) {
          if (bitCount[i] > 0) {
            exept |= (1 << i);
          }
        }
        return exept;
    }
    
    // using XOR
    public int singleNumber(int[] A) {
        int ones = 0, twos = 0;
        for(int i = 0; i < A.length; i++){
            ones = (ones ^ A[i]) & ~twos;
            twos = (twos ^ A[i]) & ~ones;
        }
        return ones;
    }
}