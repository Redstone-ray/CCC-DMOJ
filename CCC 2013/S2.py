a=int(input())
c=int(input())
b=[]
count=0
first=True
for i in range(c):
    b.append(int(input()))
for i in range(len(b)):
    if b[i]+b[i+1]+b[i+2]+b[i+3]<=a:
        if first:
            count+=4
            first=False
        else:
            count+=1
    else:
        break
print(count)