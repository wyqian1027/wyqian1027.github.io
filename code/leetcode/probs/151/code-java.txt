class Solution {

    public String reverseWords(String s) {
        s = s.trim();
        String[] strs = s.split(" ");
        StringBuilder sb = new StringBuilder();
        sb.append(strs[strs.length-1]);
        for (int i=strs.length-2; i >= 0; i--){
            if (!strs[i].equals("")){
                sb.append(" ").append(strs[i]);
            }
        }
        return sb.toString();
    }
}

//trick with "+"
public String reverseWords(String s) {
    String[] words = s.trim().split(" +");
    Collections.reverse(Arrays.asList(words));
    return String.join(" ", words);
}