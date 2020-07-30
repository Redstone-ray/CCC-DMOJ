import sys
input = sys.stdin.readline
n,a,b = int(input()),input().split(),input().split()
for i in range(n):
    position = a.index(b[i])
    if a[i] != b[position] or position == i:
        print("bad")
        break
else:
    print("good")