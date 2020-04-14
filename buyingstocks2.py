class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        selling_price, buying_price, max_profit, min_price = prices[0], prices[0], 0, prices[0]
        for i in range(1,len(prices)):
            profit_1 = prices[i] - min_price # MAX PROFIT
            profit_2 = prices[i] - buying_price + max_profit
            
            
            
            if profit_1 > max_profit:
                buying_price = prices[1]
                max_profit = profit_1
            if profit_2 > max_profit:
                buying_price = prices[1]
                max_profit = profit_2
                
            
            
            min_price = min(min_price,prices[i])
            
        return max_profit
            
            
            
            
                
            
        