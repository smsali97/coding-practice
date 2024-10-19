class Solution:
    def integerBreak(self, n: int) -> int:
        # n =  a1 + a2 + ak at least two integers
        # max(a1,a2 ,.. ak)


        # 10
        # 9 + 1 , 9  # breaking into ones not optima
        # 8 + 2, 10
        # 7 + 3, 21
        # 6 + 4, 24
        # 4 + 3 + 3 = 10
        #    (7)(3)
        #   (4,3)(3) # can only do this one

        # how to break integers
        # given integer n , break into n-1, and check how that can be broken?
        # include that number as a product or break it down furtheer

        # 10
            # 9 1
                 # 8  1 1 (n-2) (2)
                    # 7 1 1 1 (n-3) (3)
        # 8

        # 7 1 
        # 6 2 , 6 1 1
        # 5 3 , 5 2 1 -->
        # 4, 3, 1

        dp = {1: 1}
        for n1 in range(2,n+1):
            dp[n1] = n1 if n1 != n else 0 # you can keep the broken number itself if it wasnt the original number
            for n2 in range(1,n1):
                val = dp[n2] * dp[n1-n2] # we can compute this because n-n1 < n 
                dp[n1] = max(dp[n1],val)
        return dp[n]
        
                

        
          