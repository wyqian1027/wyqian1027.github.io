class Solution {
    
    String[] front = {"1", "6", "9", "8", "0"};
    String[] back  = {"1", "9", "6", "8", "0"};
    
    public List<String> findStrobogrammatic(int n) {
        
        if (n == 0) return null;
        if (n == 1) return new ArrayList<>(Arrays.asList("0", "1", "8"));
        if (n == 2) return new ArrayList<>(Arrays.asList("11", "69", "96", "88"));
        
        List<String> res = (n % 2 == 1 ? new ArrayList<>(Arrays.asList("0", "1", "8")):
                           new ArrayList<>(Arrays.asList("00", "11", "69", "96", "88")));
        
        List<String> ans;
        while (n > 2) {
            ans = new ArrayList<>();
            int range = (n - 2 <= 2 ? 4: 5);
            for (String str: res){
                for (int i =0 ; i < range; i++){
                    ans.add(front[i] + str + back[i]);
                }
            }
            res = ans;     
            n -= 2;
        }
        
        return res;       
    }
}