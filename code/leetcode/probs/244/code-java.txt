class WordDistance {

    private Map<String, List<Integer>> map;
    
    public WordDistance(String[] words) {
        map = new HashMap<>();
        for (int i=0; i < words.length; i++){
            String w = words[i];
            if (!map.containsKey(w)){
                map.put(w, new ArrayList<>());
            }
            map.get(w).add(i);
        }  
    }
    
    public int shortest(String word1, String word2) {
        Integer dist = Integer.MAX_VALUE;
        for (Integer i: map.get(word1)){
            for(Integer j: map.get(word2)){
                dist = Math.min(dist, Math.abs(i -j));
            }
        }
        return dist;
    }
}

/**
 * Your WordDistance object will be instantiated and called as such:
 * WordDistance obj = new WordDistance(words);
 * int param_1 = obj.shortest(word1,word2);
 */