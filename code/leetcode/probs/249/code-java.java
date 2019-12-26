class Solution {
    public List<List<String>> groupStrings(String[] strings) {

        List<List<String>> res = new ArrayList<>();
        Map<String, List<String>> map = new HashMap<>();
        
        int n = strings.length;
        
        for (int i = 0; i < n; i++){
            
            char[] arr = strings[i].toCharArray();
            int offset = arr[0] - 'a';
            
            for (int j = 0; j< arr.length; j++){
                arr[j] -= offset;
                if (arr[j] < 'a') arr[j] += 26;
            }
            
            String serial = new String(arr);
            if (!map.containsKey(serial)){
                map.put(serial, new ArrayList<String>());
            }
            map.get(serial).add(strings[i]);
        }
        
        for (Map.Entry<String, List<String>> entry: map.entrySet()){
            res.add(entry.getValue());
        }
        
        return res;
    }
}