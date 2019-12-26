class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[0] - o2[0];
            }
        });
        
        int prev = 0;
        for (int i = 0; i < intervals.length; i++){
            if (intervals[i][0] < prev) return false;
            prev = intervals[i][1];
        }
        return true;
    }
}