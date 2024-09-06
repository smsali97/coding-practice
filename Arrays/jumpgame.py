class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_index = len(nums) - 1
        for i in reversed( range(0, curr_index) ):
            if i + nums[i] >= curr_index:
                curr_index = i
        return curr_index == 0