class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        # get maximum of two types
        types_seen_at = {}

        max_size = 0

        while r < len(fruits):
            fruit_type = fruits[r]
            if fruit_type in types_seen_at:
                types_seen_at[fruit_type] = r
                r += 1
                max_size = max(r - l, max_size)
            elif len(types_seen_at) < 2:
                types_seen_at[fruit_type] = r
                r += 1
                max_size = max(r - l, max_size)
            else:
                # reduce window
                if fruits[l] in types_seen_at and types_seen_at[fruits[l]] == l:
                    del types_seen_at[fruits[l]]
                l += 1
        return max_size



        
