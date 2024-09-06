class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [[0]*(target+1) for i in range(len(nums)+1)]
        for i in range(len(dp)-1,-1,-1):
            for j in range(len(dp[i])):
                dp[i][j] += dp[i+1][rem + num]
                dp[i][j] += dp[i+1][rem + (-1*num)]

        return dp[0][0]            

        # two choices
            # +-
            # choices in nums
        mem = {}
        def rec(rem=0,i=0):
            if (rem,i) in mem: return mem[(rem,i)]
            if i == len(nums): return 1 if rem == target else 0
            ways = 0
            num = nums[i]
            ways += rec(rem + num, i+1)
            ways += rec(rem + (-1*num), i+1)
            mem[(rem,i)] = ways
            return ways
        
        return rec()
            