class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = [nums[0]]
        rsum = [nums[-1]]
        for i in range(1,len(nums)):
            lsum.append(lsum[i-1] + nums[i])
        for i in range(len(nums)-2,-1,-1):
            rsum.append(rsum[-1] + nums[i])

        # rsum = rsum[::-1]

        for i in range(0,len(nums)):
            if lsum[i] == rsum[len(nums)-1-i]: return i
        return -1

