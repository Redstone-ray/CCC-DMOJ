import sys
input = sys.stdin.readline

H = int(input())

for i in range(H // 2):
    print('*' * (i * 2 + 1) + ' ' * (2 * H - 2 * (i * 2 + 1)) + '*' * (i * 2 + 1))
print('*' * (H * 2))
for i in reversed(range(H // 2)):
    print('*' * (i * 2 + 1) + ' ' * (2 * H - 2 * (i * 2 + 1)) + '*' * (i * 2 + 1))