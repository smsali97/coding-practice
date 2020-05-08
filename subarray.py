from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ctr = 0
        curr_sum = 0
        sums_so_far = defaultdict(int)
        for num in nums:
            curr_sum += num
            
            if curr_sum == k:
                ctr += 1
            
            if curr_sum - k in sums_so_far:
                ctr += sums_so_far[curr_sum - k]
            
            sums_so_far[curr_sum] = sums_so_far[curr_sum] + 1
            
        return ctr
        