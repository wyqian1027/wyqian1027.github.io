class Solution {
    public int[][] merge(int[][] intervals) {
        
        if (intervals.length == 0) return intervals;
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[0] - o2[0];
            }
        });
        
        int ptr = 0;
        int[][] res = new int[intervals.length][2];
        res[0] = intervals[0];
        for (int i = 1; i < intervals.length; i++){
            if (res[ptr][1] >= intervals[i][0]){
                res[ptr][1] = Math.max(res[ptr][1], intervals[i][1]);
            } else {
                ptr++;
                res[ptr] = intervals[i];
            }
        }
        
        return Arrays.copyOf(res, ptr+1);
    }
}