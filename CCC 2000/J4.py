a=int(input())
l=[]
for s in range(a):
    b=int(input())
    l.append(b)
while True:
    c=int(input())
    if c==77:
        break
    if c==99:
        i=int(input())
        split=int(input())
        a=l[i-1]*split//100
        b=l[i-1]-a
        l.pop(i-1)
