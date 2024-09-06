class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # A A A B B B (order doesnt matter)
        # n = 2

        # A B - A B - A B

        # greedy?
        # 4 As 3 Bs

        # pick most frequent letter from the heap
            # check its cooldown period is bnasically the iteration coun
        # letter -> starts at

        # (frequency, letter)

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1 
            if maxHeap:
                max_val = heapq.heappop(maxHeap)
                cnt = 1 + max_val
                if cnt: q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
        