class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        from collections import defaultdict
        adj_list = defaultdict(list)
        for src, dst in connections:
            adj_list[src].append((dst, 1))  # 1 denotes original direction
            adj_list[dst].append((src, 0))  # 0 denotes reversed direction

        comes_from_zero = {0}
        reversals = 0
        visited = set()

        def dfs(node):
            reversals = 0
            visited.add(node)

            for neighbor, direction in adj_list[node]:
                if neighbor not in visited:
                    if direction == 1:  # Need to reverse
                        reversals += 1
                    comes_from_zero.add(neighbor)
                    reversals += dfs(neighbor)
            return reversals

        return dfs(0)
