## Leetcode 121 - Best Time to Buy and Sell Stocks
## Nov. 25, 2023

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, prices[0]
        for sell in prices:
            profit = max(profit, sell - buy)
            buy = min(buy, sell)
        return profit

    def maxProfit1(self, prices: List[int]) -> int:
        # use the two pointers technique
        profit, buy, sell = 0, 0, 1
        while sell < len(prices):
            profit = max(prices[sell] - prices[buy], profit)
            buy = sell if prices[buy] > prices[sell] else buy
            sell += 1
        return profit
