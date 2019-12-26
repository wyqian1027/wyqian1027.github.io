class Solution {
    public String removeDuplicateLetters(String s) {
        
        int[] counts = new int[26];
        char[] arr = s.toCharArray();
        
        for (int i=0; i < arr.length; i++){
            counts[arr[i]-'a']++;
        }
        
        Stack<Character> stack = new Stack<>();
        int[] set = new int[26];
                
        for (int i = 0; i < arr.length; i++){
            
            char cur = arr[i];
            counts[cur - 'a']--;
            
            if (set[cur - 'a'] == 1) continue;
            
            while(!stack.isEmpty() && stack.peek() > cur && counts[stack.peek() - 'a'] > 0){
                set[stack.pop() - 'a']--;
            }
            stack.push(cur);
            set[cur - 'a']++;            
        }
        
        String ans = "";
        while (!stack.isEmpty()){
            ans = stack.pop() + ans;
        }
        
        return ans;
    }
}