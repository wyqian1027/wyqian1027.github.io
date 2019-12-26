// improved by using HashSet

class Solution {
    
    public String reverseVowels(String s) {
        
        char[] arr = s.toCharArray();
        // String vowels = "aeiouAEIOU";
        Set<Character> set = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        int left = 0, right = arr.length - 1;
        while (left < right){
            
            // while (left < right && !vowels.contains(arr[left] + "") ){
            while (left < right && !set.contains(arr[left]) ){
                left++;
            }
            // while (left < right && !vowels.contains(arr[right] + "") ){
            while (left < right && !set.contains(arr[right]) ){
                right--;
            }
            reverse(arr, left++, right--);
            
        }
        return new String(arr);
    }
    
    private void reverse(char[] arr, int i, int j){
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }
}