class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0 
        stack = [] # (starts_at, height)
        for i,h in enumerate(heights):
            start = i
            # need to keep stack in increasing order
            while stack and stack[-1][1] > h:
                last_index, last_height = stack.pop()
                max_area = max(max_area, (i-last_index)*last_height)
                start = last_index
            
            stack.append((start,h))
        
        while stack:
            start, height = stack.pop()
            max_area = max(max_area, (len(heights) - start)*height)
        
        return max_area


