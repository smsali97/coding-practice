class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # I: [2,7,11,15]  target=9
        # O: [2,7] -> [1,2] # only one pair , no dup.
        
        # l has the lesser number, right has the greater side
        # depending on which way the sum is tilted towards we
        # will adjust those pointers accordingly

        l = 0
        r = len(numbers) - 1

        while l < r: # because you need two indexes
            curr_sum = numbers[l] + numbers[r]
            if curr_sum < target:
                # we are getting less than we need increase left
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                print(numbers[l],numbers[r])
                return [l+1,r+1]
        
        return [-1,-1] # should not occur