    public int maxProfitOneTransaction(int[] p) {

        if (p.length<=1) return 0;
        int profit = 0;
        int min = p[0];
        for (int i=0; i < p.length; i++){
            min = Math.min(min, p[i]);
            profit = Math.max(profit, p[i]-min);
        }
        return profit;
    }