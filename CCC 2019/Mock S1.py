a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
print('{0:.1f}'.format(sum(b)/len(b)))