// Leetcode 121 - Best Time to Buy and Sell Stocks
// Nov. 25, 2023

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let profit = 0, buy = prices[0];
    for (let sell of prices) {
        profit = Math.max(profit, sell - buy);
        buy = Math.min(buy, sell);
    }
    return profit;
}

var maxProfit1 = function(prices) {
    let profit = 0, buy = 0, sell = 1;
    while (sell < prices.length) {
        let gains = prices[sell] - prices[buy];
        profit = gains > profit ? gains : profit;
        buy = prices[buy] > prices[sell] ? sell : buy;
        sell++;
    }
    return profit;
};