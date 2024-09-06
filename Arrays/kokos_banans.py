class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # at least h has to be the number of piles

        # try out multiple values of k, and check if koko can eat it
        # recur on left and right side based on if its possible

        def can_koko_eat_it(k: int, piles: List[int], h: int):
            from math import ceil
            hours_required = 0
            for pile in piles:
                hours_required += ceil(pile/k)

            print(hours_required,h,k)
            return hours_required <= h

        l = 1
        r = max(piles)
        min_eating_speed = float('inf')
        while l <= r:
            k  = (l+r)//2
            can_eat = can_koko_eat_it(k,piles,h)
            if can_eat:
                min_eating_speed = min(min_eating_speed,k)
                r = k - 1
            else:
                l = k + 1

        return min_eating_speed