a=int(input())
b=input()
ac=0
bc=0
for i in range (a):
    if b[i]=="A":
        ac+=1
    else:
        bc+=1
if ac==bc:
    print("Tie")
elif ac>bc:
    print("A")
else:
    print("B")
