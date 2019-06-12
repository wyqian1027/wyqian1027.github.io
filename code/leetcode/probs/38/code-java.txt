class Solution {
    public String countAndSay(int n) {
        
        StringBuilder sb = new StringBuilder();
        sb.append('1');
        
        while (n > 1){
            char[] seq = sb.toString().toCharArray();
            sb = new StringBuilder();
            int count = 0;
            char cur = seq[0];
            
            for (int i = 0; i < seq.length; i++){
                if (seq[i] == cur){
                    count++;
                } else {
                    sb.append(String.valueOf(count)).append(cur);
                    cur = seq[i];
                    count = 1;
                }
            }
            sb.append(String.valueOf(count)).append(cur);
            n--;
        }
        return sb.toString();
    }
}