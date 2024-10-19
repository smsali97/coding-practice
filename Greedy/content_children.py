class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
         # max. content children
         #   content IFF size[j] >= g[i]
         # cookie can be used only once   
        #  h = 1 2 3
        #  s = 1,1

        #  h = 10,20
        #  s = 1,2,3
        #  1-1, 2-2



        # start from largest size if it doesnt satiate anyone it means were done
        # iterate through hunger levels and check where it matches start fromt he next index

        hunger = sorted(g,reverse=True)
        sizes = sorted(s,reverse=True)

        j = 0
        satisfied_ctr = 0
        # T O(S log S + G log G)
        # S O(n) TODO O(1) if inplace
        for i, largest_size in enumerate(sizes): 
            hunger_met = False
            while not hunger_met and j < len(hunger):
                if largest_size >= hunger[j]:
                    hunger_met = True
                    satisfied_ctr += 1
                j += 1
        return satisfied_ctr 




