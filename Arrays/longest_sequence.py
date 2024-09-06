class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a starting point of consecutive series is if
        # there is no left-most element
        uniq_nums = set(nums)
        longest_consecutive = 0
        for n in nums:
            is_leftmost = n-1 not in uniq_nums
            if is_leftmost:
                series = 1
                x = n+1
                while x in uniq_nums:
                    series += 1
                    x += 1
                longest_consecutive = max(longest_consecutive, series)
        return longest_consecutive