def test(i, j, dir):
    pi = i
    pj = j
    k = 0
    while pi >= 0 and pi < r and pj >= 0 and pj < c and grid[pi][pj] in (".", "*") and k < n:
        if m[k] == "R":
            dir = abs(dir - 90)
        elif m[k] == "L":
            dir = (dir + 90) % 360
        elif m[k] == "F":
            if dir == 0:
                pj += 1
            elif dir == 180:
                pj -= 1
            elif dir == 90:
                pi -= 1
            else:
                pi += 1
        k += 1
    if k >= n and pi >= 0 and pi < r and pj >= 0 and pj < c and grid[pi][pj] == '.':
        grid[pi][pj] = "*"
r, c = int(input()), int(input())
grid = []
for i in range(r):
    grid.append([])
for i in range(r):
    line = input()
    for j in range(c):
        grid[i].append(line[j])
n = int(input())
m = []
for i in range(n):
    m.append(input())
for i in range(r):
    for j in range(c):
        for d in range(0, 360, 90):
            test(i, j, d)
print('\n'.join(map(''.join, grid)))