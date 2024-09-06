class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index_possible = 0
        for i in range(len(nums)):
            # if my maximum jump cannot cross i
            if i > max_index_possible: return False
            max_index_possible = max(max_index_possible,i + nums[i]) 
        return True