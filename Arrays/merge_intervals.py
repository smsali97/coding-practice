class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_intervals = []
        intervals.sort()

        if len(intervals) <= 1:
            return intervals
        def overlaps(i1,i2): return i2[0] <= i1[1]
        def merge(i1,i2): return ( min(i1[0],i2[0]), max(i1[1],i2[1]) )
        interval1 = intervals[0]
        i = 1
        while i < len(intervals):
            interval2 = intervals[i]
            if overlaps(interval1,interval2):
                interval1 = merge(interval1,interval2)
            else:
                merged_intervals.append(interval1)
                interval1 = interval2
            i += 1
        if len(merged_intervals) < len(intervals):
            merged_intervals.append(interval1)
        return merged_intervals


