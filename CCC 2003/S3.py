'''
105
14
16
IIIIIIIIIIIIIIII
I......I.......I
I......III.....I
I........I.....I
I........IIIIIII
IIIIIIIIII.....I
I.I......I.....I
III..III.I.....I
I....I.IIIII...I
I....I.....III.I
I....I.......I.I
I....I.....III.I
I....I.....I...I
IIIIIIIIIIIIIIII

105
5
16
IIIIIIIIIIIIIIII
I...IIIIII.....I
I...IIIIII.....I
I...IIIIII.....I
IIIIIIIIIIIIIIII

10
5
4
IIII
I..I
IIII
I..I
IIII

'''

# find connected components
# bfs, dfs, union-find

'''
{
(3,1): [ (3,2)]
(3,2): [ (3,1)]
}
'''


def getNeighbour(curr):
    nb = []

    r, c = curr
    if r - 1 >= 0 and rooms[r - 1][c] != 'I':
        nb.append((r - 1, c))
    if r + 1 < row and rooms[r + 1][c] != 'I':
        nb.append((r + 1, c))
    if c + 1 < col and rooms[r][c + 1] != 'I':
        nb.append((r, c + 1))
    if c - 1 >= 0 and rooms[r][c - 1] != 'I':
        nb.append((r, c - 1))
    return nb


n = int(input())  # wood
row = int(input())
col = int(input())

rooms = []
for r in range(row):
    rooms.append(list(input()))

# build graph
graph = {}
for r in range(row):
    for c in range(col):
        if rooms[r][c] != 'I':
            neighbours = getNeighbour((r, c))
            if (r, c) not in graph:
                graph[(r, c)] = neighbours
            else:
                graph[(r, c)].extend(neighbours)

            for nb in neighbours:
                if nb not in graph:
                    graph[nb] = []
                graph[nb].append((r, c))


#
def bfs(n):
    visited = {n}
    q = [n]

    while q:
        node = q.pop(0)

        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
    return visited


#
room_size = []
while graph:
    k = list(graph.keys())[0]
    room = bfs(k)
    print(k)

    size = len(room)
    room_size.append(size)

    for n in room:
        r, c = n
        rooms[r][c] = '*'
        graph.pop(n)

    for r in rooms:
        print(*r, sep='')

print(room_size)