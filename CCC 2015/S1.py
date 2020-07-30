a=[]
for y in range(int(input())):
    x=int(input())
    if x:
        a.append(x)
    else:
        a.pop()
print(sum(a))
