class Solution {
    public int countPrimes(int n) {
        
    // Original Approach:
    //     int count = 0;
    //     for (int x = 2; x < n; x++) {
    //         boolean isPrime = true;
    //         for (int i = 2; i < x; i++){
    //             if (x % i == 0) {
    //                 isPrime = false;
    //                 break;
    //             }   
    //         }
    //         count += isPrime ? 1 : 0;
    //     }
    //     return count;
    // }
    
        if (n < 2) return 0;
        int[] res = new int[n]; // from 0 to n-1
                                // 1 => not prime, 0 => prime 
                                
        for (int i = 2; i < Math.sqrt(n); i++){ //Math.sqrt used since only half numbers need check
            if (res[i] == 0) {
                for (int j = 2*i; j < n; j+=i){
                    res[j] = 1;
                }
            }
        }
        
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (res[i] == 0) count += 1;
        }
        return count;
    }
}