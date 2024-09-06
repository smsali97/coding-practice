# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        # start off with the max width rectangle
        i = 0
        j = len(height) - 1
        while i < j:
            width = j - i
            # rectangle of water is bounded by the minimum height
            min_height = min(height[i],height[j])
            # keep track of max in case the increase in height doesnt compensate the previously higher width
            max_area = max(max_area,min_height * width)
            # if j is better than i, you are better off moving i pointer
            if height[j] > height[i]: i += 1
            else: j -= 1
        return max_area
        