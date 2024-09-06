class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1,len(nums)):
            for j in range(i,0,-1):
                if nums[j-1] == 0:
                    nums[j-1], nums[j] = nums[j] , nums[j-1]
                else:
                    break
    
a = [0,1]
Solution().moveZeroes(a)
print(a)
        