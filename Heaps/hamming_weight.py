class Solution:
    def hammingWeight(self, n: int) -> int:
        ctr = 0
        while n > 0:
            n, r = divmod(n,2)
            if r == 1: ctr += 1
        return ctr