class Solution {
    public String getPermutation(int n, int k) {
        
        StringBuilder sb = new StringBuilder();
        List<Integer> nums = new LinkedList<>();
        for (int i = 1; i <= n; i++) nums.add(i);
        
        k -= 1;
        int end = n;
        for (int i = 0; i < end; i++){
            
            int factor = factorial(n-1);
            int index = k / factor;
            k = k % factor;
            
            sb.append(String.valueOf(nums.get(index)));
            nums.remove(index);
            n -= 1;            
        }
        return sb.toString();        
    }
        
    
    private int factorial(int n) {
        if (n == 0 || n == 1) return 1;
        return n*factorial(n-1);
    }
}