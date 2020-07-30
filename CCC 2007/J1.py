a,b,c = int(input()),int(input()),int(input())

if a != min(a, b, c) and a != max(a, b, c):
    print(a)
elif b != min(a, b, c) and b != max(a, b, c):
    print(b)
else:
    print(c)