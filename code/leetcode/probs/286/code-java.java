class Solution {
    public void wallsAndGates(int[][] rooms) {
        
        if (rooms == null || rooms.length == 0 || rooms[0].length == 0) return;
        
        // find all gates
        int m = rooms.length;
        int n = rooms[0].length;
        Deque<int[]> queue = new ArrayDeque<>();
        
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (rooms[i][j] == 0){
                    queue.offer(new int[]{i, j});
                }
            }
        }
        
        int[] ir = new int[]{0, 0, -1, 1};
        int[] ic = new int[]{-1, 1, 0, 0};
        
        while (!queue.isEmpty()){
            int[] pair = queue.poll();
            int r = pair[0], c = pair[1], depth = rooms[r][c] + 1;
            for (int i = 0; i < 4; i++){
                int nr = r + ir[i];
                int nc = c + ic[i];
                if (0 <= nr && nr < m && 0 <= nc && nc < n && rooms[nr][nc] == Integer.MAX_VALUE){
                    rooms[nr][nc] = depth;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
    }
}