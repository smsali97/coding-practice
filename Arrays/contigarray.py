class Solution:
    def findMaxLength(self, nums: list) -> int:
        
        # The code leverages the concept of a prefix sum and a hashmap to efficiently 
        # find balanced subarrays. By treating 1s as +1 and 0s as -1,
        # the running sum curr_sum helps identify subarrays where the net change is 0,
        # indicating an equal number of 0s and 1s. The hashmap stores the indices of 
        # previously encountered curr_sum values, allowing for quick calculation of 
        # subarray lengths when the same curr_sum is seen again.

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
        
        