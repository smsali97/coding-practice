# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.


# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums = []) -> int:
        max_product = nums[0] if len(nums) >= 1 else 0
        current_product = nums[0] if len(nums) >= 1 else 0

        for i in range(1,len(nums)):
            current_product = max(nums[i],nums[i] * current_product)

            max_product = max(max_product, current_product)

        return max_product

s = Solution()
print(s.maxProduct([-2,0,-1]))
print(s.maxProduct([2,3,-2,4]))