// Leetcode 121 - Best Time to Buy and Sell Stocks
// Nov. 25, 2023

// refactored for efficiency
int maxProfit(int* prices, int pricesSize) {
    if (pricesSize == 0) return 0;

    int profit = 0, buy = prices[0];

    for (int sell = 1; sell < pricesSize; sell++) {
        profit = prices[sell] - buy > profit ? prices[sell] - buy : profit;
        buy = buy > prices[sell] ? prices[sell] : buy;
    }
    return profit;
}

// original
int maxProfit1(int* prices, int pricesSize) {
    int profit = 0, buy = 0, sell = 0;
    while (sell < pricesSize) {
        int gains = prices[sell] - prices[buy];
        profit = gains > profit ? gains : profit;
        buy = buy > sell ? sell : buy;
        sell++;
    }
    return profit;
}