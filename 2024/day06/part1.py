

import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip()))


def func():

    rows, cols = len(grid), len(grid[0])
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '^':
                start = (r,c)
                break

    r,c = start
    d = 0
    ans = 0
    seen = {(start)}
    while True:
        nr, nc = r + directions[d][0],  c + directions[d][1]
        if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
            break
        if (nr, nc) not in seen and grid[nr][nc] == '.':
            seen.add((nr,nc))
        if grid[nr][nc] == '#':
            d  = (d + 1) % 4
            continue
        r, c = nr, nc
    print(len(seen))


func()      




