class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        
        for (String str: strs){
            String counts = getCharCount(str);
            if (!map.containsKey(counts)){
                map.put(counts, new ArrayList<String>());
            }
            map.get(counts).add(str);
        }
        
        for (Map.Entry<String, List<String>> entry: map.entrySet()){
            res.add(entry.getValue());
        }
        return res;
        
    }
    
    public String getCharCount(String str){
        
        int[] res = new int[26];
        for (int i = 0; i < str.length(); i++){
            res[str.charAt(i) - 'a']++;
        }
        StringBuilder sb = new StringBuilder();  
        for (int i = 0; i < 26; i++){
            sb.append(res[i]).append("-");
        }
        return sb.toString();
    }
}