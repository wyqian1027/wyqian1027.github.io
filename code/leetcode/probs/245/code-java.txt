class Solution {
    public int shortestWordDistance(String[] words, String word1, String word2) {
        int dist = words.length;
        int loc1 = -1, loc2 = -1;
        
        if (!word1.equals(word2)){
            for (int i=0; i < words.length; i++){
                if (words[i].equals(word1)){
                    loc1 = i;
                } else if (words[i].equals(word2)){
                    loc2 = i;
                }
                // System.out.println(loc1 + ", " + loc2);
                if (loc1 != -1 && loc2 != -1){
                    dist = Math.min(dist, Math.abs(loc1-loc2));
                }
            }
        } else {
            for (int i=0; i < words.length; i++){
                if (words[i].equals(word1)){
                    loc1 = loc2;
                    loc2 = i;
                }
                if (loc1 != -1 && loc2 != -1){
                    dist = Math.min(dist, loc2-loc1);
                }
            }
        }
        return dist;      
        
    }
}