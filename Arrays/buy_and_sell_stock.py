# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_cost = prices[0];
        max_profit = 0
        
        for i in range(1,len(prices)):
            min_buy_cost = min(prices[i],min_buy_cost)
            
            max_profit = max(max_profit, prices[i]-min_buy_cost)
        return max_profit