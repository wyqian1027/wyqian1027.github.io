class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        
        List< List< Integer>> res = new ArrayList<>();
        HashMap< String, Integer> map = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            map.put(words[i], i);
        }
        
        for (int i = 0; i < words.length; i++){
            String word = words[i];
            for (int j = 0; j <= word.length(); j++){
                String str1 = word.substring(0, j);
                String str2 = word.substring(j);
                if (isPal(str1)){
                    String str2rev = new StringBuilder(str2).reverse().toString();
                    if (map.containsKey(str2rev) && map.get(str2rev) != i){
                        List<Integer> pair = new ArrayList<>();
                        pair.add(map.get(str2rev));
                        pair.add(i);
                        res.add(pair);
                    }
                }
                if (isPal(str2) && str2.length() != 0){
                    String str1rev = new StringBuilder(str1).reverse().toString();
                    if (map.containsKey(str1rev) && map.get(str1rev) != i){
                        List<Integer> pair = new ArrayList<>();
                        pair.add(i);
                        pair.add(map.get(str1rev));
                        res.add(pair);
                    }
                }                
            }
        }
        return res;
    }
    
    private boolean isPal(String s){
        int l = 0, r = s.length()-1;
        while (l < r){
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
}