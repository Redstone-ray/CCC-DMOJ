import sys
input = sys.stdin.readline

T = int(input())
S = int(input())
H = int(input())

for t in range(T):
    print('*', end='')
    for s in range(S):
        print(' ', end='')
    print('*', end='')
    for s in range(S):
        print(' ', end='')
    print('*')
for s in range(2 * S + 3):
    print('*', end='')
print()
for h in range(H):
    for s in range(S + 1):
        print(' ', end='')
    print('*', end='')
    for s in range(S + 1):
        print(' ', end='')
    print()