        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        # Initialize dp array where dp[i] represents the maximum amount we can rob up to house i
        dp = [0] * len(nums)
        
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Fill in the dp array
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # The last element in dp array contains the maximum amount that can be robbed
        return dp[-1]