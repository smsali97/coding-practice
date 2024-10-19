class Solution:
    def numSquares(self, n: int) -> int:
        # min. no of perfect squares that sum to n
        # perfect square IFF y = x^2 where x is some integer

        # n=12
        # 1, 4, 9

        # 12= 9 + 1 + 1 + 1
        # 12 = 4 + 4 + 4

        # all of the perfect squares that are <= n , O(sqrt(n))
        # try out all combinations until we cannot reach 0, or completely finish n
        perfect_squares = []
        import math
        for m in range(1,math.ceil(math.sqrt(n))+1):
            if m*m<=n: perfect_squares.append(m*m)
        cache = {}
        def rec(num_remaining=n):
            if num_remaining == 0: return 0
            if num_remaining in cache: return cache[num_remaining]
            options = []
            for candidate in perfect_squares: 
                if num_remaining - candidate < 0: continue # no more possible deductions
                options.append(1 + rec(num_remaining-candidate))
            ans = min(options) if len(options) else float('inf')
            cache[num_remaining] = ans
            return ans
        least_number = rec()
        return -1 if least_number == float('inf') else least_number
