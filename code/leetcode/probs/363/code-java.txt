class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        
        if (matrix == null || matrix.length == 0) return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int res = Integer.MIN_VALUE;
        
        for (int left = 0; left < n; left++){
            
            int [] sums = new int[m];
            
            for (int right = left; right < n; right++){
            
                for (int i = 0; i < m; i++){
                    sums[i] += matrix[i][right];
                }
                
                TreeSet<Integer> set = new TreeSet<>();
                set.add(0);
                int curSum = 0;
                
                for (int sum: sums){
                    curSum += sum;
                    Integer x = set.ceiling(curSum - k);
                    if (x != null) res = Math.max(res, curSum - x);
                    set.add(curSum);
                }
            }
        }
        return res;

    }
}