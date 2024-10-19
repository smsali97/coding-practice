class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        

        l, r = 0, 0

        zeroes_found = 0
        curr_length = 0
        max_length = 0
        while l <= r and r < len(nums):
            if nums[r] == 0:
                zeroes_found += 1
            
            while zeroes_found > 1:
                if nums[l] == 0: zeroes_found -= 1
                l += 1
            
            max_length = max(max_length,r-l)
            r += 1
        return max_length