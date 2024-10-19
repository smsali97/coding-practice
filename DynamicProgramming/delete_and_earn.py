class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        unique_nums = sorted(count)
        n = len(unique_nums)

        # Initialize DP array
        dp = [0] * (n + 1)  # dp[i] stores max earnings up to the ith unique number

        for i in range(n):
            curr_num = unique_nums[i]
            curr_gain = curr_num * count[curr_num]

            if i > 0 and unique_nums[i - 1] == curr_num - 1:
                dp[i + 1] = max(dp[i], dp[i - 1] + curr_gain)
            else:
                dp[i + 1] = dp[i] + curr_gain

        return dp[n]