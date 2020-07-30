from collections import defaultdict
time = -1
list = []
dict = {}
sentDict={}
timeDict= defaultdict(int)
for i in range(int(input())):
    a, b = input().split()
    b = int(b)
    if a != "W":
        time += 1
    else:
        time += b - 1
    if a == "R":
        dict[b] =time
        sentDict[b]=False
    if a=="S":
        if b in dict:
           timeDict[b]=timeDict[b]+time-dict[b]
        else:
            timeDict[b]=time-dict[b]
        sentDict[b]=True

for k,b in sorted(sentDict.items()):
    if b==False:
        print(k,-1)
    else:
        print(k,timeDict[k])

