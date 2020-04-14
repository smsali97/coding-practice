class Solution:
    def findMaxLength(self, nums: list) -> int:
        
        max_length = 0
        
        curr_sum = 0
        hmap = {}
        for i in range(0,len(nums)):
            x = 1 if nums[i] is 1 else -1
            
            curr_sum += x
            if curr_sum is 0:
                max_length = i+1
            
            if curr_sum in hmap:
                max_length = max(i - hmap[curr_sum],max_length)
            else:
                hmap[curr_sum] = i
        
        
        return max_length
        
        