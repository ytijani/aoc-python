


import sys

grid =  []
for line in sys.stdin:
    grid.append(list(line.strip()))




def func(grid):

    rows, cols = len(grid), len(grid[0])
    ans = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 'A':
                continue

            if r - 1 < 0 or c - 1 < 0 or r + 1 >= rows or c + 1 >= cols:
                continue
            diag1 = grid[r-1][c-1]  + 'A' + grid[r + 1][c + 1]
            diag2 = grid[r-1][c + 1] + 'A' +  grid[r + 1][c - 1]
            if diag1 in ('MAS', 'SAM') and diag2 in ('MAS', 'SAM'):
                ans += 1

    print(ans)


func(grid)
