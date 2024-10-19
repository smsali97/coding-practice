class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
# Imagine you have a deque like this: [index_of_5, index_of_3, index_of_1]. This represents a window where 5 is the current maximum, followed by 3 and 1.

# Now, let's say a new element 7 enters the window. Here's why we pop the smaller elements from the back:

# 7 is the new maximum:  Since 7 is larger than all existing elements in the deque, it's guaranteed to be the maximum in the current window and any future window that includes it.

# 5, 3, and 1 are obsolete: The elements 5, 3, and 1 are now irrelevant.

# They are smaller than 7, so they can't be the maximum in any future window as long as 7 is present.
# Even if 7 eventually leaves the window, these smaller elements will also leave the window before 7 does. So, they'll never have a chance to become the maximum again.
        from collections import deque
        q = deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
                # will never become the maximum
        result = []
        for i in range(k,len(nums)):
            result.append(nums[q[0]])
            # if you are at index i and you can only have k elements
            # then your index at best can be i-1, i-2, i-3, i-k
            while q and q[0] <= i-k:
                q.popleft()
            
            # found a greater maximum, remove them from the back
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        result.append(nums[q[0]])       
        return result

            


 
        
        
        # maxes = []
        # from collections import heapq
        # for i in range(len(nums)-k+1):
        #     curr_max = max(nums[i:i+k])
        #     maxes.append(curr_max)
        # return maxes # O(n*k)

        from heapq import heappush, heappop
        
        # Initialize a max-heap to store elements within the window
        max_heap = [(-num, i) for i, num in enumerate(nums[:k])]  # Store as (-num, i) to create a max-heap
        heapify(max_heap)
        
        result = [-max_heap[0][0]]  # Store the maximum from the first window
        
        for i in range(k, len(nums)):
            # Add the new element to the heap
            heappush(max_heap, (-nums[i], i))
            
            # Remove elements that are outside the current window
            while max_heap[0][1] <= i - k:
                heappop(max_heap)
            
            # The top of the heap now contains the maximum element in the current window
            result.append(-max_heap[0][0])
        
        return result


        