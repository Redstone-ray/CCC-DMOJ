a=int(input())
x,y=[],[]
for i in range (a):
    xs,ys=map(int, input().split(","))
    x.append(xs)
    y.append(ys)
x1,y1=min(x)-1,min(y)-1
x2,y2=max(x)+1,max(y)+1
print(f"{x1},{y1}")
print(f"{x2},{y2}")