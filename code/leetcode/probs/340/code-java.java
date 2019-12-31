class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        
        if (k == 0) return 0;
            
        Map<Character, Integer> window = new HashMap<>();
        int longest = 0, j = 0;
        
        for (int i = 0; i < s.length(); i++) {
            
            char ch = s.charAt(i);
            window.put(ch, i);

            while (j <= i && window.size() > k) {
                if (window.get(s.charAt(j)) == j)
                    window.remove(s.charAt(j));
                j++;
            }
            
            longest = Math.max(longest, i - j + 1);  
        }
        
        return longest;
    }
}