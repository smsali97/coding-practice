class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {len(s): 1}
        valid_second_digits = [str(n) for n in range(10,27)]
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0': dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if i < len(s) + 1 and s[i:i+2] in valid_second_digits:
                    dp[i] += dp[i+2]
        return dp[0]

        # cache = {len(s) : 1}
        # def rec(i):
        #     if i in cache: return cache[i]
        #     # if you find a zero on its own then its 0
        #     if s[i]== '0': return 0

        #     # first digit
        #     res = rec(i+1)
        #     # add second digit if its valid
        #     valid_second_digits = [str(n) for n in range(10,27)]
        #     if i < len(s) + 1 and s[i:i+2] in valid_second_digits:
        #         res += rec(i+2)
            
        #     cache[i] = res
        #     return res
        # return rec(0)

