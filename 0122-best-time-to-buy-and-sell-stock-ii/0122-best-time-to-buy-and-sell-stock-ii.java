class Solution {
    public int maxProfit(int[] prices) {
        int profit = 0;
        for (int i = 0; i < prices.length - 1; i++) {
            int gain = prices[i + 1] - prices[i];
            if (gain > 0) {
                profit += gain;
            }
        }
        return profit;
    }
}