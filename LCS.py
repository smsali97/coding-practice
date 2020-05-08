class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R = len(text1)+1
        C = len(text2)+1
        dp = [ [0] * C for _ in range(R)]
        for i in range(1,R):
            for j in range(1,C):
                dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1] else max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]        
        