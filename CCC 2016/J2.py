# numbers = []
#
# for i in range(4):
#     numbers.append([int(x) for x in input().split()])
#
# sumx = sum(numbers[0])
#
# for i in range(4):
#     if sum(numbers[i]) == sumx:
#         if sum([row[i] for row in numbers]) == sumx:
#             pass
#         else:
#             print ("not magic")
#             sys.exit(0)
#     else:
#         print ("not magic")
#         sys.exit(0)
# print('magic')

# ///////////////////////////////////
l=[]
for i in range(4):
    l.append(input().split())
ss=set()
for row in range (4):
    s=0
    for col in range (4):
        s+=int(l[row][col])
    ss.add(s)
for col in range (4):
    s=0
    for row in range (4):
        s+=int(l[row][col])
    ss.add(s)
if len(ss)==1:
    print("magic")
else:
    print("no magic")
for a in range (4,0):
        print(l[a][a])