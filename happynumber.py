class Solution:
    def isHappy(self, n: int):
        oneThere = False
        seen = set()
        while ( not n in seen):
            if n in seen:
                break
            else:
                seen.add(n)
            n = sum([(int(x))**2 for x in str(n)])
            if n is 1:
                oneThere = True
                break
        return oneThere