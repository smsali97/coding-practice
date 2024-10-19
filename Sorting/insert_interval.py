class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # determine if interval overlaps 
        # assumes s1,e1 < s2,e2
            # if s2 < e1: min(s1,s2) max(e1,e2)
        def merge(i1,i2): return ( min(i1[0],i2[0]), max(i1[1],i2[1]) )
        mergedIntervals = []
        for i,interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                # ends before this even starts
                # this comes before the other intervals
                # rest of the intervals can be inserted in order
                mergedIntervals.append(newInterval)
                mergedIntervals.extend(intervals[i:])
                return mergedIntervals
            elif newInterval[0] > interval[1]:
                # starts after this has ended
                mergedIntervals.append(interval)
            else:
                newInterval = merge(interval,newInterval)

        # if were here we didnt add new interval just yet
        mergedIntervals.append(newInterval)
        return mergedIntervals
            