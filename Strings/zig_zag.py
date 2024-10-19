class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # P
        #   A
        #     Y
        
        # i=0

        # r=0,1,2

        # r=2,1,0

        if numRows == 1:
            return s

        row_strings = [[] for _ in range(numRows)]
        go_down = True
        i,r,n=0,0,len(s)
        while i < n:
            row_strings[r].append(s[i])
            i += 1

            if go_down:
                r += 1
            else:
                r -= 1
            
            if r == numRows:
                r = numRows-2
                if numRows < 2:
                    r = 0
                go_down = False
            if r == -1:
                r = 1
                go_down = True
        
        return ''.join([''.join(row) for row in row_strings])


