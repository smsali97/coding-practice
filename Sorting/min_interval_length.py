"""
1 2 3 4 5 6
-------
    -----
    -------
        -
"""
from sortedcontainers import SortedList
from collections import defaultdict

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        Finds the minimum-sized interval from 'intervals' that contains each query in 'queries'.
        """

        # Define event types for clarity
        START, END = 1, -1 

        # Store events: (position, event_type, interval)
        events = defaultdict(list)  
        
        # Collect all unique points (interval endpoints and queries) for the sweep line
        unique_points = set(queries)
        for left, right in intervals:
            events[left].append((START, [left, right]))
            events[right + 1].append((END, [left, right]))
            unique_points.add(left)
            unique_points.add(right + 1)

        # Store the answer for each query
        answers = defaultdict(int)  
        
        # SortedList to keep active intervals sorted by their length (shortest first)
        active_intervals = SortedList(key=lambda interval: interval[1] - interval[0]) 

        # Sweep the line across all unique points
        for point in sorted(unique_points):
            # Process events at this point
            if point in events:
                for event_type, interval in events[point]:
                    if event_type == START:
                        active_intervals.add(interval)
                    else:  # END event
                        active_intervals.remove(interval)

            # If there are active intervals, store the size of the shortest one
            answers[point] = active_intervals[0][1] - active_intervals[0][0] + 1 if active_intervals else -1

        # Retrieve answers for the original queries
        return [answers[query] for query in queries]