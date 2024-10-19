import math
from collections import Counter

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        class UnionFind:
            def __init__(self, nums):
                self.parent = {num: num for num in nums}
                self.rank = {num: 1 for num in nums}

            def find(self, num):
                if num not in self.parent:  # Check if the key exists
                    self.parent[num] = num  # Add the missing key with itself as the parent
                    self.rank[num] = 1     # Initialize the rank for the new key
                if self.parent[num] == num: 
                    return num
                self.parent[num] = self.find(self.parent[num])  # Path compression
                return self.parent[num]

            def union(self, u, v):
                root_u, root_v = self.find(u), self.find(v)
                if root_u == root_v: 
                    return
                if self.rank[root_u] > self.rank[root_v]:
                    self.parent[root_v] = root_u
                    self.rank[root_u] += self.rank[root_v]
                else:
                    self.parent[root_u] = root_v
                    self.rank[root_v] += self.rank[root_u]

        uniq_nums = set()
        edges = []
        for a in nums:
            for i in range(2, int(math.sqrt(a) + 1)):
                if a % i == 0:
                    uniq_nums.add(a)
                    uniq_nums.add(i)
                    uniq_nums.add(a // i)
                    edges.append((a, i))
                    edges.append((a, a // i))

        unionFind = UnionFind(uniq_nums)
        for e in edges: 
            unionFind.union(*e)

        c = Counter([unionFind.find(num) for num in nums])  # Use find() to get the root
        return max(c.values())  # Directly return the maximum count