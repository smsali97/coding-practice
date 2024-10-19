class Solution:
    def tribonacci(self, n: int) -> int:
        # dp = [0]*(n+1)
        # for i in range(1,n+1):
        #     if i in (1,2): dp[i] = 1
        #     else: dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        # return dp[n]

        if n == 0:
            return 0
        if n <= 2:
            return 1

        trib0, trib1, trib2 = 0, 1, 1
        for _ in range(3, n + 1):
            trib0, trib1, trib2 = trib1, trib2, trib0 + trib1 + trib2
        return trib2

        