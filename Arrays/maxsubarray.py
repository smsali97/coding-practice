class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sum = -sys.maxsize + 1
        curr_sum = 0
        
        for i in range(0,len(nums)):
            curr_sum = max(nums[i],curr_sum + nums[i]) # to add or not to add
            max_sum = max(max_sum,curr_sum) # global max
            
        return max_sum