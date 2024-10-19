class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 0: return 0
        if len(nums) < k: return sum(nums)/len(nums)
        start = 0
        end = k - 1
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for end in range(end+1,len(nums)):
            curr_sum += nums[end]
            curr_sum -= nums[start]

            max_sum = max(max_sum,curr_sum)
            start += 1
        return max_sum / k
