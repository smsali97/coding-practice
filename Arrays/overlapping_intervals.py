class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key= lambda x: x[0])
        # 1,3  
        #    2    6   
        #            8 10
        #                  15 18

        # st2 < et1  min, max
        i = 0
        modified_intervals = []
        while i < len(intervals) - 1:
            interval1 = intervals[i]
            interval2 = intervals[i+1]

            is_overlapping = interval2[0] <= interval1[1]
            if is_overlapping:
                new_interval = ( min(interval1[0],interval2[0])
                                 ,max(interval1[1],interval2[1]) )
                
                intervals[i] = new_interval
                del intervals[i+1]
            else:
                i += 1
        return intervals
