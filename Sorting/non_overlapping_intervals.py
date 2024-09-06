class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
 
        # for al interval
            # to remove
            # or not to remove
                # check if it overlaps
        def overlaps(i1,i2): return i2[0] < i1[1]
        intervals.sort()
        if len(intervals) <= 1: return 0

        first_interval = intervals[0]

        min_overlaps = 0
        for i in range(1,len(intervals)):
            second_interval = intervals[i]
            
            if overlaps(first_interval,second_interval):
                min_overlaps += 1
                print(first_interval,second_interval)
            
                if second_interval[1] < first_interval[1]:
                    first_interval = second_interval
            else:
                first_interval = second_interval 
        return min_overlaps          
            



