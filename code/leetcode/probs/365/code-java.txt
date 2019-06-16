// BFS approach
class Solution {
    
    Set<String> visited = new HashSet<>();
    
    public boolean canMeasureWater(int x, int y, int z) {
        
        if (z > x + y) return false;
        
        if (x > y) {
            int tmp = x;
            x = y;
            y = tmp;
        }
        
        Queue<int[]> queue = new LinkedList<>();
        int[] init = new int[]{0, 0};
        queue.add(init);
        visited.add(init[0] + "-" + init[1]);
        
        while (!queue.isEmpty()){
            int[] pair = queue.poll();
            int a = pair[0], b = pair[1];
            int s = a + b;
            if (a + b == z) return true;
            
            List<int[]> operations = new ArrayList<>();
            operations.add(new int[]{a, y});
            operations.add(new int[]{x, b});
            operations.add(new int[]{a, 0});
            operations.add(new int[]{0, b});
            operations.add(new int[]{Math.min(s, x), s < x ? 0 : s - x}); // pour jar y to x;
            operations.add(new int[]{s < y ? 0 : s - y, Math.min(s, y)}); // pour jar x to y

            for (int[] xy: operations){
                String e = xy[0]+"-"+xy[1];
                if (!visited.contains(e)){
                    queue.offer(xy);
                    visited.add(e);
                }
            }
        }
        return false;
    }
}

//Math Approach with GCD
class Solution {

    public boolean canMeasureWater(int x, int y, int z) {
        if (z < 0 || z > x + y) return false;
        if (z == 0) return true;
        return z % gcd(x, y) == 0;
    }
    
    private int gcd(int x, int y){
        if (y == 0) return x;
        return gcd(y, x % y);
    }
}