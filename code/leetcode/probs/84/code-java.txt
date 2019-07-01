// O(NlogN) Divide and Conquer

class Solution {
    public int largestRectangleArea(int[] heights) {
    
        return largestRectangleArea(heights, 0, heights.length -1);
    }
    
    public int largestRectangleArea(int[] heights, int left, int right) {
        
        if (left > right) return 0;
        if (left == right) return heights[left];
        int minIndex = findMinIndex(heights, left, right);
        int ans = heights[minIndex] * (right - left + 1);
        ans = Math.max(ans, largestRectangleArea(heights, left, minIndex - 1));
        ans = Math.max(ans, largestRectangleArea(heights, minIndex + 1, right));
        return ans;
    }
    
    private int findMinIndex(int[] heights, int left, int right){
        int minIndex = left;
        for (int i = left; i <= right; i++){
            if (heights[i] < heights[minIndex]){
                minIndex = i;
            }
        }
        return minIndex;
    }
}