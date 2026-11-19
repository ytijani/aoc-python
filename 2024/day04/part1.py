


import sys

grid =  []
for line in sys.stdin:
    grid.append(list(line.strip()))




def func(grid):

    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0), (0,1),(0,-1),(1,0), (1,1),(-1,-1),(1,-1),(-1,1)]
    ans = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 'X':
                continue

            for dr, dc in directions:
                word = ""
                for step in range(4):
                    nr, nc = r + dr * step, c + dc * step
                    if not (0 <= nr < rows and 0 <= nc < cols):
                        break
                    word += grid[nr][nc]
                if word == 'XMAS':
                    ans += 1
    print(ans)


func(grid)
