class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        seen = set()

        def dfs(jug1, jug2):  # Keep track of both jugs
            if jug1 + jug2 == targetCapacity:
                return True
            if (jug1, jug2) in seen or jug1 < 0 or jug1 > jug1Capacity or jug2 < 0 or jug2 > jug2Capacity:
                return False

            seen.add((jug1, jug2))  # Store the state as a tuple

            return (
                dfs(jug1Capacity, jug2) or  # Fill jug1
                dfs(0, jug2) or  # Empty jug1
                dfs(jug1, jug2Capacity) or  # Fill jug2
                dfs(jug1, 0) or  # Empty jug2
                dfs(max(0, jug1 - (jug2Capacity - jug2)), min(jug2Capacity, jug2 + jug1)) or  # Pour jug1 to jug2
                dfs(min(jug1Capacity, jug1 + jug2), max(0, jug2 - (jug1Capacity - jug1)))  # Pour jug2 to jug1
            )

        return dfs(0, 0)  # Start with both jugs empty