class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for amount_required in range(1,len(dp)):
            for c in coins:
                change = amount_required - c
                if change < 0: continue
                dp[amount_required] = min(1 + dp[change],dp[amount_required])
        
        return dp[-1] if dp[-1] != float('inf') else -1

