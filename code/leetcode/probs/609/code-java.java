class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
    
        HashMap<String, List<String>> map = new HashMap<>();
        
        for (String path: paths){
            String[] splitStr = path.split(" ");
            String curPath = splitStr[0];
            for (int i = 1; i < splitStr.length; i++){
                String[] pair = splitStr[i].split("\\(");
                String filename = pair[0];
                String content = pair[1].substring(0, pair[1].length()-1);
                if (!map.containsKey(content)) map.put(content, new ArrayList<String>());
                map.get(content).add(curPath + "/" + filename);
                // System.out.println(map);
            }
        }
        List<List<String>> res = new ArrayList<>();
        for (List<String> group: map.values()) {
            if (group.size() > 1)
                res.add(group);
        }
        return res;
    }
}