class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for i in range(len(text1)+1)  ]

        #    a  b  c  d  e
        # a  1  0  0  0  0
        # c  0  1  2  2  2
        # e  0  1  2  2  3

        # up , left, and diagonal if match

        # Base cases (first row and column are already 0)

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                match = 1 if text1[i - 1] == text2[j - 1] else 0  # Adjust indices
                dp[i][j] = max(dp[i - 1][j - 1] + match, dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]  # Or dp[len(text1)][len(text2)]

                
