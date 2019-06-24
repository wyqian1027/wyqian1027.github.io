// 1. Using Heap, sort by start time

class Solution {
    
    public int minMeetingRooms(int[][] intervals) {
        
        if (intervals.length == 0) return 0;
        
        PriorityQueue<Integer> pq = 
            new PriorityQueue<>(intervals.length,
                new Comparator<Integer>(){
                    @Override
                    public int compare(Integer o1, Integer o2){
                        return o1 - o2;    
                    }
                });
        
        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[0] - o2[0];
            }
            });
        
        pq.offer(intervals[0][1]);
        for (int i = 1; i < intervals.length; i++){
            if (pq.peek() <= intervals[i][0]) pq.poll();
            pq.offer(intervals[i][1]);
        }
        return pq.size();
    }
}

// 2. Using two Pointers on start array and end array

class Solution {

    public int minMeetingRooms(int[][] intervals){
        
        if (intervals.length == 0) return 0;
        
        int[] startArr = new int[intervals.length];
        int[] endArr = new int[intervals.length];
        
        for (int i = 0; i < startArr.length; i++) startArr[i] = intervals[i][0];
        for (int i = 0; i < endArr.length; i++) endArr[i] = intervals[i][1];
        
        Arrays.sort(startArr);
        Arrays.sort(endArr);
        
        int startPtr = 0, endPtr = 0;
        int numRooms = 0;
        
        for (int i = 0; i < intervals.length; i++){
            if (endArr[endPtr] <= startArr[startPtr]){
                numRooms--;
                endPtr++;
            }
            numRooms++;
            startPtr++;
        }
        
        return numRooms;        
    }
}