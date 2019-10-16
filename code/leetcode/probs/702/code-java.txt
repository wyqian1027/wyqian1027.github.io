class Solution {
    public int search(ArrayReader reader, int target) {
        
        int l = 0, r = 1;
        
        while (l < r) {
            
            int rightValue = reader.get(r);
            int leftValue = reader.get(l);
            
            if (leftValue == 2147483647 && rightValue == 2147483647) break;
            
            if (target > rightValue) {
                l = r;
                r = 2*r;
            } else {
                int m = l + (r - l) / 2;
                int midValue = reader.get(m);

                if (midValue == target) {
                    return m;
                } else if (midValue < target) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }
        
        return reader.get(l) == target ? l : -1;
    }
}