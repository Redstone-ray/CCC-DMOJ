import sys
input = sys.stdin.readline

a = [1, 2, 3, 4, 5, 6, 7]
b = []
c = [(1, 7), (1, 4), (2, 1), (3, 4), (3, 5)]

while True:
    x, y = int(input()), int(input())
    if x == 0 and y == 0:
        break
    else:
        c.append((x, y))
for i in range(7):
    for j in a:
        for k in c:
            if j == k[1]:
                if k[0] in a:
                    break
        else:
            b.append(j)
            a.remove(j)
            break
    else:
        print('Cannot complete these tasks. Going to bed.')
        break
else:
    print(*b)
