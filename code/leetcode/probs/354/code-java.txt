// N^2 Approach

class Solution {
    public int maxEnvelopes(int[][] dolls) {

        if (dolls == null || dolls.length == 0) return 0;
        
        Arrays.sort(dolls, new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                if (o1[0] == o2[0]){
                    return o1[1] - o2[1]; // both ascending
                } else {
                    return o1[0] - o2[0];
                }
            }
        });
           
        int[] dp = new int[dolls.length];
        int maxSofar = 0;
        
        for (int i = 0; i < dolls.length; i++){
            
            int res = 0;
            for (int j = 0; j < i; j++){
                if (dolls[j][0] < dolls[i][0] &&
                    dolls[j][1] < dolls[i][1]){
                    res = Math.max(res, dp[j]);
                }
            }
            dp[i] = res + 1;
            maxSofar = Math.max(maxSofar, dp[i]);
        }
        
        return maxSofar;
    }
}        
        
// NlogN Approach

class Solution {
    public int maxEnvelopes(int[][] dolls) {

        if (dolls == null || dolls.length == 0) return 0;
        
        Arrays.sort(dolls, new Comparator<int[]>(){
            @Override
            public int compare(int[] o1, int[] o2){
                if (o1[0] == o2[0]){
                    return o2[1] - o1[1]; //descending!!
                } else {
                    return o1[0] - o2[0];
                }
            }
        });
        
        int[] dp = new int[dolls.length];
        int len = 0;
        
        for (int[] doll: dolls){
            int index = Arrays.binarySearch(dp, 0, len, doll[1]);
            if (index < 0) index = -(index+1);
            dp[index] = doll[1];
            if (index == len) len++;
        }        
        return len;
    }
}