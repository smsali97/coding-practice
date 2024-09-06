class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        # like binary search except need to determine r,c instead of index
        # one approach is to flatten 2d matrix
        l = 0
        R = len(matrix)
        C = len(matrix[0])
        r = R*C - 1

        # 6 -> (2,2)
        # column is like the offset
        # row is the quotient?
        while l <= r:
            mid = (l+r)//2
            row = mid // C
            col = mid % C
            val = matrix[row][col]
            if target == val:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
