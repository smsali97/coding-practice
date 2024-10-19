import random

class Solution:
    def __init__(self, w: List[int]):
        self.n = len(w)
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

    def pickIndex(self) -> int:
        target = random.random() * self.prefix_sums[-1]  # Generate a random number in the range of total weight
        # Use binary search to find the index
        low, high = 0, self.n - 1
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()