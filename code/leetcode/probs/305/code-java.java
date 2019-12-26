class Solution {
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        
        int[] p = new int[m*n];
        int[][] grid = new int[m][n];
        List < Integer >  res = new ArrayList < Integer > ();
        int num = 0;
        int[][] directions = new int[][] {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
            
        for (int i = 0; i < n*m; i++) p[i] = i;
        for (int i = 0; i < positions.length; i++){
            int r = positions[i][0];
            int c = positions[i][1];            
            if (grid[r][c] == 1) {
                res.add(num);
                continue;
            };
            
            int cur = r*n + c;
            grid[r][c] = 1;
            num++;
            for (int j = 0; j < 4; j++){
                int newR = r + directions[j][0];
                int newC = c + directions[j][1];
                if (0 <= newR && newR < m && 0 <= newC && newC < n && grid[newR][newC] == 1) {
                    int nei = newR*n + newC;
                    int xp = find(cur, p);
                    int yp = find(nei, p);
                    if (xp != yp) {
                        p[xp] = yp;
                        num--;
                    }                
                }
            }
            res.add(num);
        }
        return res;
    }
    
    private int find(int node, int[] p){
        if (p[node] != node) {
            p[node] = find(p[node], p);
        }
        return p[node];
    }
}