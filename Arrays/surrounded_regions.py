class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        visit = set()
        def in_border(i,j): return any([min(i,j) == 0,i == len(board) - 1,j == len(board[i]) - 1])
        def valid_cell(i,j): return i in range(len(board)) and j in range(len(board[i]))
        def get_neighbors(i,j):
            neighbors = []
            for dx, dy in directions:
                if valid_cell(dx+i,dy+j): neighbors.append([dx+i,dy+j])
            return neighbors

        def dfs(i,j):
            border_cells_with_o.add((i,j))
            for new_i, new_j in get_neighbors(i,j):
                if board[new_i][new_j] != 'O': continue
                if (new_i,new_j) in border_cells_with_o: continue
                dfs(new_i,new_j)
        
        #  capture regions that are surrounded
        #  capture all regions except those are surrounded

        # leave them out
        border_cells_with_o = set()
        for i in range(len(board)):
            for j in range(len(board[i])):
                if in_border(i,j) and board[i][j] == 'O':
                    dfs(i,j)

        # mark the rest as captured
        for i in range(len(board)):
            for j in range(len(board[i])):
                if (i,j) in border_cells_with_o: continue
                if board[i][j] == 'O': board[i][j] = 'X'
        return board



        
        
        
                    
