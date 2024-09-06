# -2 1 -3 4 -1 2 1 -5 4


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import sys
        max_so_far = -sys.maxsize
        max_ending_here = 0
        
        for i in range(len(nums)):
            # keep track of a cumulative sum
            max_ending_here += nums[i]
            
            # but wait! if you have something better, a more positive value that will
            # override the negative value
            max_ending_here = max(max_ending_here,nums[i])
            
            # keep track of a global maximum incase your max_ending_here goes down
            max_so_far = max(max_so_far,max_ending_here)
        
        return max_so_far
            
            
            
            