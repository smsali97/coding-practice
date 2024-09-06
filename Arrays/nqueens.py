class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # rows have to be different
        # cols have to be different
        # diagnoal have to be different
        #   0 1
        # 0 Q .
        # 1 . Q
        # (1 - 0)/(1-0) => 1

        #   0 1
        # 0 . Q
        # 1 Q .
        # (0 - 1)/(1-0) => -1

        #   4 5
        # 2 . Q
        # 3 Q .
        # (2-3)/(5-4) => -1
        
        # for every row aka Queen
        #     do until q > 0
        #     if queen == 0: save this board!
        #     check if queen is placed right
        #     fix a col 'c'
        #     recur on Q-=1
        #     backtrack this queen

        cols = set()
        queens = set() # tuples of (r,c)
        board = [['.']*n for _ in range(n)]
        solutions = []
        
        def lies_in_diagonal(queens,r,c):
            x1, y1 = c, r
            for y2, x2 in queens:
                 # gradient
                gradient= abs((y2-y1)/(x2-x1))
                if gradient == 1: return True
            return False

        def dfs(r=0):
            if r == n:
                board_str = [''.join(row) for row in board]
                solutions.append(board_str)
                return
            for c in range(n):
                if c in cols or lies_in_diagonal(queens,r,c):
                    continue
                cols.add(c)
                queens.add((r,c))
                board[r][c] = 'Q'
                print(r,c)

                # explore
                dfs(r+1)
                # cleanup for backtrack
                queens.remove((r,c))
                board[r][c] = '.'
                cols.remove(c)
        dfs()
        return solutions


            


          
    