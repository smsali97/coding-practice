class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n+1)]
        for i in range(len(dp)):
            q, r = divmod(i,2)
            dp[i] = r + dp[q]
        return dp
