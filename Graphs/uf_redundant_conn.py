class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class UnionFind:
            def __init__(self,elements):
                self.parent = {el: el for el in elements}
                self.rank = {el: 1 for el in elements}
            
            def find(self, node: int):
                if self.parent[node] == node:
                    return node # you are the parent
                self.parent[node] = self.find(self.parent[node]) # path compression
                return self.parent[node]
                # grand parent if exists
            
            def unionByRank(self, u: int, v: int):
                root_u, root_v = self.find(u), self.find(v)
                if root_u == root_v:
                    return True 

                if self.rank[root_u] > self.rank[root_v]:
                    self.parent[root_v] = root_u
                    self.rank[root_u] += self.rank[root_v]
                else:
                    self.parent[root_u] = root_v
                    self.rank[root_v] += self.rank[root_u]
                return False
            
        nodes = set([node for edge in edges for node in edge])
        unionFind = UnionFind(nodes)
        for edge in edges:
            u,v = edge
            if unionFind.unionByRank(u,v):
                # already same set
                return edge
        return [] # not possible
        
        