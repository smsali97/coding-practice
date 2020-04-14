
grid = []
for line in open('puzzles'):
    grid.append(line.split())


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            print(str(i+1)+ ' ' + str(j+1))
