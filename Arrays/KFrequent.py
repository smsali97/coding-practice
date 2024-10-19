class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict

        d = defaultdict(int)
        for n in nums:
           d[n] += 1
        

        sorted_items = sorted(d.items(),key=lambda x: x[1],reverse=True)
        return [x[0] for x in sorted_items[:k]]