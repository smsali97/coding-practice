class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        can_reach_pacific = set()
        can_reach_atlantic = set()

        ROWS, COLS = len(heights), len(heights[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def rec(r,c,visit,prev_height=None):
            if not prev_height: prev_height = heights[r][c]
            visit.add((r,c))

            for dx, dy in directions:
                i, j = r + dx, c + dy
                if i not in range(ROWS) or j not in range(COLS): continue
                if (i,j) in visit: continue
                if heights[i][j] < heights[r][c]: continue
                rec(i,j,visit,heights[r][c])
        for row in range(ROWS):
            rec(row,0,can_reach_pacific)
            rec(row,COLS-1,can_reach_atlantic)
        for col in range(COLS):
            rec(0,col,can_reach_pacific)
            rec(ROWS-1,col,can_reach_atlantic)
        return can_reach_pacific.intersection(can_reach_atlantic)
