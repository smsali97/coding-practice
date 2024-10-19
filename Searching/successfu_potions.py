class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        
        """
        for each spell find the number of potions it can successfully make
        """
        potions.sort()
        # successful IFF spells[i] x potions[j] >= success
        def successful(i,j): return spells[i] * potions[j] >= success
        successful_pairs = []
        for spell_idx, spell in enumerate(spells):
            
            success_ctr = 0
            # binary search potions
            l, r = 0, len(potions) - 1
            while l <= r:
                potion_idx = (l+r)//2
                successful_pair = successful(spell_idx,potion_idx)
                if successful_pair:
                    success_ctr += (r - potion_idx + 1)
                    r = potion_idx - 1
                else:
                    l = potion_idx + 1
            successful_pairs.append(success_ctr)
        return successful_pairs




        