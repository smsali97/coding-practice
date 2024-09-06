class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}
        def rec(i=0,j=0):
            if (i,j) in cache: return cache[(i,j)]
            # base case
            if j == len(t): return 1
            if i == len(s): return 0 # exhausted all options
            # two choices
            # we pick if char matches
            opt1 = rec(i+1,j+1) if s[i] == t[j] else 0
            # or not pick
            opt2 = rec(i+1,j) # since we didnt succesfully match j remains same
            cache[(i,j)] = opt1 + opt2
            return opt1 + opt2
        # pick that character or not (i)
        # t will if we have reached the end  or not
        return rec()