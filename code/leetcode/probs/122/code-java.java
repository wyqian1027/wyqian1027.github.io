    public int maxProfitAsManyTransactions(int[] prices) {

        if (prices.length <= 1) return 0;

        int profit = 0;
        int prev = prices[0];
        for (int i=1; i < prices.length; i++){
            int cur = prices[i];
            if (prev < cur) profit += (cur-prev);
            prev = cur;
        }
        return profit;
    }