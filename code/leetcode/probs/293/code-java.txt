class Solution {
    public List<String> generatePossibleNextMoves(String s) {
        
        List<String> res = new ArrayList<>();

        if (s == null || s.length() < 2) return res;
        
        char[] arr = s.toCharArray();
        for (int i=0; i < arr.length - 1; i++){
            if (arr[i] == '+' && arr[i+1] == '+'){
                arr[i] = arr[i+1] = '-';
                res.add(new String(arr));
                arr[i] = arr[i+1] = '+';
            }
        }
        return res;
    }
}