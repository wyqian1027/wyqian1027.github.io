class Solution {
    public String minWindow(String s, String t) {
        
        int[] tMap = new int[128];
        int[] window = new int[128];
        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();
        int required = 0;
        for (char ch: tArr){
            tMap[ch]++;
        }
        for (int x: tMap){
            required = x > 0 ? required + 1 : required;
        }
        int l = 0, r = 0;
        int formed = 0;
        int minL = Integer.MAX_VALUE;
        int candL = 0, candR = 0;
        
        while (r < sArr.length){
            
            char rChar = sArr[r];
            window[rChar]++;
            if (tMap[rChar] > 0 && window[rChar] == tMap[rChar]){
                formed++;
            }
            while (formed == required && l <= r){
                char lChar = sArr[l];
                if (r - l + 1 < minL){
                    minL = r - l + 1;
                    candL = l;
                    candR = r;
                }
                l++;
                if (tMap[lChar] > 0 && window[lChar] == tMap[lChar]){
                    formed--;
                }
                window[lChar]--;
            }
            r++;
        }
        return minL == Integer.MAX_VALUE ? "" : s.substring(candL, candR+1);
    }
}