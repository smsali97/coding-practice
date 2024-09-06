class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # Gas:  +1  +2   +3   +4   +5
        # Cost:   -3   -4   -5   -1   -2

        #      -2 --> -2 --> -2 --> +3 --> +3 
        # imposible iff running total < 0
        # 2   3  4 
        # 3   4  3
        # -1 -1  1
        n = len(gas)
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            if curr_tank < 0:
                starting_station = i + 1  # Potential new starting point
                curr_tank = 0
        return starting_station if total_tank >= 0 else -1 
        # avoid a cycle by visiting n stations
        # brute force
        for i in range(n):
            # start at multiple i's
            tank = 0
            ctr = 0
            index = i
            while ctr < n:
                tank += gas[index]
                tank -= cost[index]
                if tank < 0: break
                ctr += 1
                index = (i + ctr) % n
            if tank >= 0: return index
        return -1
