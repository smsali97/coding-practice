class Solution:
    def search(self, nums: List[int], target: int) -> int:


       # Rotation can be between (l,m) (m,h) or even m as well!
       # if pivot is on RHS , LHS is sorted can compare with that!
       #                LHS , RHS is sorted!

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l+r)//2
            mid_val = nums[mid]
            start_val = nums[l]
            end_val = nums[r]

            if target == mid_val: return mid
                
            # left half is sorted?
            if start_val <= mid_val:
                # check if target lies between start and mid
                if start_val <= target <= mid_val:
                    r = mid - 1
                else:
                    l = mid + 1 # pivot on other side

            # right half is sorted?
            if mid_val <= end_val:
                if mid_val <= target <= end_val:
                    l = mid + 1 
                else:
                    r = mid - 1 # check the pivoted side
        return -1