class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        memo = {}  # For memoization

        def recursive_count(dice_left, remaining_target):
            if dice_left == 0:
                return 1 if remaining_target == 0 else 0  # Base case

            if (dice_left, remaining_target) in memo:
                return memo[(dice_left, remaining_target)]

            ways = 0
            for face in range(1, k + 1):
                if remaining_target >= face:
                    ways = (ways + recursive_count(dice_left - 1, remaining_target - face)) % mod

            memo[(dice_left, remaining_target)] = ways
            return ways

        return recursive_count(n, target)