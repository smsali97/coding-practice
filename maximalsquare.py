class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        D = len(matrix)
        if D == 0: return 0
        C = len(matrix[0])
        dp = [[0] * C for _ in range(D)]
        maxA = 0
        for i in range(D):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                maxA = 1
        for i in range(C):
            if matrix[0][i] == '1':
                dp[0][i] = 1
                maxA = 1
        for i in range(1,D):
            for j in range(1,C):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1],min(dp[i-1][j-1],dp[i-1][j])) + 1
                maxA = max(dp[i][j],maxA)
        return maxA ** 2