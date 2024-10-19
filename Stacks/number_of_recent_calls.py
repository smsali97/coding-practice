class RecentCounter:

    def __init__(self):
        self.requests = []
    def ping(self, t: int) -> int:
        self.requests.append(t)

        ctr = 0
        last_index = len(self.requests) - 1
        while last_index >= 0 and self.requests[last_index] >= t - 3000:
            ctr += 1
            last_index -= 1    
        return ctr
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)