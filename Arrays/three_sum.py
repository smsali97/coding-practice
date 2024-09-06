class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # I: [-1,0,1,2,-1,-4]
        # O: [[-1,-1,2],[-1,0,1]]

        # -1+2 --> 1 [ -1 to balance it out] ,   -1
        # sorting helps? because then  you can tell how much you need
        # I: [-4,-2,-2,0,2,4,6]
        # O: 
        triplets = []
        nums.sort()
        for i,v1 in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums)-1
            while l < r:
                tSum = nums[l] + nums[r] + nums[i]
                if tSum > 0:
                    r -= 1
                elif tSum < 0:
                    l += 1
                else:
                    triplets.append([nums[l] , nums[r] , nums[i]])
                    l += 1 # right will adjust itself no need to handle
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return triplets


