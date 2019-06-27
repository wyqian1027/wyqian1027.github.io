// from top to bottom

 Solution {
    public int minimumTotal(List<List<Integer>> A) {
        
        int n = A.get(A.size()-1).size();
        int[] row = new int[n];
        row[0] = A.get(0).get(0);
        
        for (int i = 1; i < A.size(); i++){
            // using descending so that we dont need prev
            for (int j = i; j >= 0 ; j--){
                int lowest = Integer.MAX_VALUE;
                if (j != 0) {
                    lowest = Math.min(lowest, row[j-1]);
                }
                if (j != i) {
                    lowest = Math.min(lowest, row[j]);
                }
                row[j] = A.get(i).get(j) + lowest;
            }
        }
        
        int ans = row[0];
        for (int i = 1; i < row.length; i++) ans = Math.min(ans, row[i]);
        return ans;
    }
}

// from bottom to top, easier corner cases
class Solution {
    public int minimumTotal(List<List<Integer>> A) {
        
        int n = A.get(A.size()-1).size();
        int[] row = new int[n+1];
        
        for (int i = A.size() - 1; i >= 0; i--){

            for (int j = 0; j <= i ; j++){
                int lowest = Integer.MAX_VALUE;
                lowest = Math.min(lowest, row[j]);
                lowest = Math.min(lowest, row[j+1]);

                row[j] = A.get(i).get(j) + lowest;
            }
        }
        return row[0];
    }
}