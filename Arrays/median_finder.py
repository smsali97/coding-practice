class MedianFinder:
    from heapq import heappush, heappop

    def __init__(self):
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        heappush(self.small,-num)

        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heappop(self.small)
            heappush(self.large,val)
        
        if len(self.small) > len(self.large):
            val = -heappop(self.small)
            heappush(self.large,val)
        if len(self.small) < len(self.large):
            val = heappop(self.large)
            heappush(self.small,-val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (-self.small[0] + self.large[0])/2 


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()