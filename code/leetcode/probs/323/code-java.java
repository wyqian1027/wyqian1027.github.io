class Solution {
    public int countComponents(int n, int[][] edges) {
        
        int[] p = new int[n];
        int num = n;
        
        for (int i = 0; i < n; i++) p[i] = i;
        for (int[] pair: edges){
            int xp = find(pair[0], p);
            int yp = find(pair[1], p);
            if (xp != yp) {
                p[xp] = yp;
                num--;
            }
        }
        return num;
    }
    
    private int find(int node, int[] p){
        if (p[node] != node) {
            p[node] = find(p[node], p);
        }
        return p[node];
    }
}