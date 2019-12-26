class Solution {
    public String largestNumber(int[] nums) {
    
        String[] strArr = new String[nums.length];
        for (int i = 0; i < nums.length; i++) strArr[i] = String.valueOf(nums[i]);
        
        Arrays.sort(strArr, new Comparator<String>(){
            @Override
            public int compare(String a, String b){
                String order1 = a + b;
                String order2 = b + a;
                return -order1.compareTo(order2);
            }
        });
        
        if (strArr[0].equals("0")) return "0";
        StringBuilder sb = new StringBuilder();
        for (String str: strArr){
            sb.append(str);
        }
        return sb.toString();
    }
}