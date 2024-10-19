class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num = second_num = float('inf')  # Initialize to positive infinity
        
        for num in nums:
            if num <= first_num:
                first_num = num
            elif num <= second_num:
                second_num = num
            else:
                return True  # Found an increasing triplet
        
        return False  # No increasing triplet found