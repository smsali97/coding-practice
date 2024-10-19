class Solution:
    def findMinArrowShots(self, intervals: List[List[int]]) -> int:
        """
        1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
          -------------
        -----------
                    -----------
        +1 +2     1 2  1       0

            ------
        -------
            ------
        1   3 2  0

        case 1: if two intervals are non overlapping then we need an arrow for the first one at least
        case 2: if they are overllaping then take the overlapping region and this will be your new
        'interval' to compare

        """        
        intervals.sort()

        if len(intervals) <= 1: return len(intervals)

        last_interval = intervals[0]

        def overlaps(i1,i2):
            return i2[0] <= i1[1]

        def get_overlapping_region(i1,i2):
            return ( max(i1[0],i2[0]), min(i1[1],i2[1])   )

        arrows_needed = 0
        had_overlap_previously = False
        for interval in intervals:
            if not overlaps(last_interval,interval):
                arrows_needed += 1
                last_interval = interval
            else:
                last_interval = get_overlapping_region(last_interval,interval)
        return arrows_needed + 1
        """
        1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6
          -------------
        -----------
                    -----------
        """

        
        


        