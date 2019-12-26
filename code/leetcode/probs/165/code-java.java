class Solution {
    public int compareVersion(String version1, String version2) {
        
        int i1 = 0, i2 = 0;
        int n1 = version1.length(), n2 = version2.length();
        
        while (i1 < n1 || i2 < n2){
            
            int s1 = i1, s2 = i2;
            int sub1 = 0, sub2 = 0;
            while (s1 < n1 && version1.charAt(s1) != '.') s1++;
            while (s2 < n2 && version2.charAt(s2) != '.') s2++;
            if (i1 < n1) {
                sub1 = Integer.valueOf(version1.substring(i1, s1));
            }
            if (i2 < n2) {
                sub2 = Integer.valueOf(version2.substring(i2, s2));
            }
            if (sub1 < sub2) return -1;
            if (sub1 > sub2) return 1;
            i1 = s1 + 1;
            i2 = s2 + 1;
        }
        
        return 0;
    }
}