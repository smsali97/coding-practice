class Solution:

    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+1)]

        
        for i in range(n-1,-1,-1):
            for buy in (0,1):
                opt1, opt2 = float('-inf'), float('-inf')
            
                # buy the stock
                if buy: opt1 = -prices[i] -fee + dp[i+1][0]
                # sell the stock
                if not buy: opt2 = prices[i] + dp[i+1][1]
                # do nothing
                opt3 = dp[i+1][buy]
                ans = max(opt1,opt2,opt3)
                dp[i][buy] = ans
        return dp[0][1] # we can buy




        mem = {}
        def rec(i=0,buy=1):
            if (i,buy) in mem: return mem[(i,buy)]
            if i >= n: return 0 # base case cannot choose more

            opt1, opt2 = float('-inf'), float('-inf')
            
            # buy the stock
            if buy: opt1 = -prices[i] -fee + rec(i+1,buy=0)
            # sell the stock
            if not buy: opt2 = prices[i] + rec(i+1,buy=1)
            # do nothing
            opt3 = rec(i+1,buy)
            ans = max(opt1,opt2,opt3)
            mem[(i,buy)] = ans
            return ans
        return rec()
