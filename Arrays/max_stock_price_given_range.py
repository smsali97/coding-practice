# Q: Given a array of stock prices, find the max stock prices for the given second range.

from typing import List
import heapq

def solve(prices: List[int], second: int):
    heap = []
    L = 0
    R = 0
    max_price = float('-inf')

    while L < len(prices):
        if len(heap) < second:
            # you can explore further
            heapq.heappush(heap,-prices[R])
            R += 1
        else:
            # limit reached try to remove now
            current_max = -heapq.heappop(heap)
            heapq.heappush(heap,-prices[L])
            max_price = max(max_price,current_max)
            L += 1
            print(L,R,max_price,heap)
    
    if len(heap) > 0:
        max_price = max(max_price,-heapq.heappop(heap))

    return max_price
	

# main
if '__main__' == __name__:
    prices = [17,20,19,4,9,10,12,24]
    second = 3
    print(solve(prices,second))

