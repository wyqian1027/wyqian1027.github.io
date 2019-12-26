class Solution {
    public int minHeightShelves(int[][] books, int shelfWidth) {
        int[] dp = new int[books.length + 1]; 
        dp[0] = 0; // no book
        for (int i = 0; i < books.length; i++){
            int curW = books[i][0];
            int curH = books[i][1];
            int ans = dp[i] + curH;
            for (int j = i-1; j >= 0 && curW + books[j][0] <= shelfWidth; j--){
                curW += books[j][0];
                curH = Math.max(curH, books[j][1]);
                ans = Math.min(curH + dp[j], ans);  // dp[j] => ans for j-1 th book, the prev book of j
            }
            dp[i+1] = ans;            
        }
        return dp[books.length];
    }
}