class Solution {
    public int nthUglyNumber(int n) {
        
        PriorityQueue<Long> pq = new PriorityQueue<>();        
        Set<Long> seen = new HashSet<>();
        
        seen.add(1L);
        pq.offer(1L);
        int[] candidates = new int[]{2, 3, 5};
        
        while (n > 1) {
            Long x = pq.poll();
            for (int c: candidates) {
                if (!seen.contains(x*c)) {
                    pq.offer(x*c);
                    seen.add(x*c);
                }
            }
            n--;
        }
        return (int) (long) pq.poll();
    }
}