class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        chosen_indices == k

        max( sum * min )
        """

        import heapq

        # Pre-calculate pairs of (nums2[i], nums1[i]) and sort in descending order of nums2[i]
        pairs = sorted(zip(nums2, nums1), reverse=True)
        max_heap = []
        current_sum = 0
        max_score = 0

        for num2, num1 in pairs:
            heapq.heappush(max_heap, num1)
            current_sum += num1
            if len(max_heap) > k:
                current_sum -= heapq.heappop(max_heap)
            if len(max_heap) == k:
                max_score = max(max_score, current_sum * num2)

        return max_score