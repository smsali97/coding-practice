class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # numbers aka choice from 1-9
        # limit in size k, and must sum up to 9

        number_choices = [n for n in range(1,10)]
        total_combinations = []
        def rec(i=0, numbers=set()):
            curr_sum, size = sum(numbers), len(numbers)
            if curr_sum == n and size == k:
                total_combinations.append(numbers)
                return # success!
            if size == k:
                return # fail! cannot add more :()
            if i == len(number_choices):
                return

            # to include or not to include

            # opt1
            rec(i+1, numbers | {number_choices[i]})
            # opt2
            rec(i+1,numbers)
        
        rec()
        return total_combinations








    
