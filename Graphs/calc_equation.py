class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        a / b =  2 
        b / c =  3

        a --> b = 2
        b --> c = 3        
        """
        from collections import defaultdict
        adj_list = defaultdict(list)
        for equation, ans in zip(equations,values):
            first, second = equation
            adj_list[first].append(  (second, ans)  )
            adj_list[second].append(  (first, 1/(ans) )  )

        print(adj_list)
        def solve(src, target):
            if src not in adj_list.keys(): return float('inf')
            if target not in adj_list.keys(): return float('inf')
            if src == target: return 1
            visited.add(src)
            for nei, val in adj_list[src]:
                if nei in visited: continue
                ans = val * solve(nei, target)
                if ans != float('inf'): return ans
            return float('inf') # invalid choice
        
        answers =  []
        for query in queries:
            visited = set()
            ans = solve(*query)
            if ans == float('inf'): ans = -1
            answers.append(ans)
        return answers
            
        