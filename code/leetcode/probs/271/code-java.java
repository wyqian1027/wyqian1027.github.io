// Ways of encoding: 3#abc
// Or: replace "#" by "##", use " # " for separation

public class Codec {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for (String str: strs){
            sb.append(String.valueOf(str.length())).append("#").append(str);
        }
        return sb.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String s) {
        
        List<String> res = new ArrayList<>();
        int i = 0;
        while (i < s.length()){
            
            int j = s.indexOf("#", i);
            int strLen = Integer.valueOf(s.substring(i, j));
            res.add(s.substring(j+1, j+1+strLen));
            i = j+1+strLen;
        }
        return res;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(strs));