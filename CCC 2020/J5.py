a, b = int(input()), int(input())
c = []
d = []
e = []
f = []
end = [a - 1, b - 1]
start = [0, 0]
breaks = False
counter = 0
dont_go = [(0, 0)]

for i in range(1, a + 1):
    for j in range(1, b + 1):
        c.append(i * j)
    d.append(c)
    c = []
for i in range(1, a + 1):
    e = input().split()
    f.append(e)
    e = []

while True:
    counter += 1
    for i in range(a):
        for j in range(b):
            if int(f[start[0]][start[1]]) == d[i][j] and not (i,j) in dont_go:
                start.clear()
                start.append(i)
                start.append(j)
                breaks = True
                break
        if breaks == True:
            breaks = False
            break
    else:
        dont_go.append((start[0],start[1]))
        start = [0, 0]

    if start == end:
        print('yes')
        break
    if counter >= 2.33*(a * b):
        print("no")
        break
