class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}
        n = len(questions)
        dp = [0]*(n+1)
        for i in range(n-1,-1,-1):
            points, brainpower = questions[i]
            opt1 = points + dp[min(i+brainpower+1,n)]
            opt2 = dp[i+1]
            dp[i] = max(opt1,opt2)
        return dp[0]    

        def rec(i=0):
            if i >= len(questions): return 0
            if i in cache: return cache[i]
            points, brainpower = questions[i]
            # take qs
            opt1 = points + rec(i+brainpower+1)
            # not take qs
            opt2 = 0 + rec(i+1)
            ans = max(opt1,opt2)
            cache[i] = ans
            return ans
        return rec()  