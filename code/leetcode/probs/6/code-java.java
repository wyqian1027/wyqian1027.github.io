class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        StringBuilder[] sb = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) sb[i] = new StringBuilder();
        int idx = 0, len = s.length();
        
        while (idx < len){
            for (int r = 0; r < numRows && idx < len; r++) {
                sb[r].append(s.charAt(idx++));
            }
            for (int r = numRows-2; r >= 1 && idx < len; r--) {
                sb[r].append(s.charAt(idx++));           
            }
        }
        
        for (int i = 1; i < numRows; i++){
            sb[0].append(sb[i].toString());
        }
        
        return sb[0].toString();
    }
}