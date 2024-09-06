class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # getting heaviest --> need max heap
        from heapq import heappush, heappop, heapify
        max_heap = [-s for s in stones]
        heapify(max_heap)

        elements_left = len(max_heap) >= 2
        while elements_left:
            y = -heappop(max_heap)
            x = -heappop(max_heap)

            if x != y:
                heappush(max_heap,-(y-x))
            elements_left = len(max_heap) >= 2

        if len(max_heap) == 0: return 0
        if len(max_heap) == 1: return -max_heap[0]
        