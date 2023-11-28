// Leetcode 121 - Best Time to Buy and Sell Stocks
// Nov. 25, 2023

#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0, buy = prices[0];
        for (int sell : prices) {
            profit = max(profit, sell - buy);
            buy = min(buy, sell);
        }
        return profit;
    }

    int maxProfit1(vector<int>& prices) {
        int profit = 0, buy = 0, sell = 0;
        while (sell < prices.size()) {
            profit = max(profit, prices.at(sell) - prices.at(buy));
            buy = prices[buy] > prices[sell] ? sell : buy;
            sell++;
        }
        return profit;
    }
};