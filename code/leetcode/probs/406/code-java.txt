class Solution {
    public int[][] reconstructQueue(int[][] people) {
        
        Arrays.sort(people, new Comparator<int[]>() {
           @Override
            public int compare(int[] o1, int[] o2){
                if (o1[0] == o2[0]) {
                    return o1[1] - o2[1];
                } else {
                    return - (o1[0] - o2[0]);
                }
            }
        });
        
        List<int[]> res = new LinkedList<>();
        
        for (int[] person: people){
            res.add(person[1], person);
        }
        
        // int[][] ans = new int[people.length][]; int i = 0;
        // for (int[] pair: res){
        //     ans[i++] = pair;
        // }
        
        return res.toArray(new int[people.length][]);
    }
}