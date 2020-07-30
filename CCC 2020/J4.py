a=input()
b=input()
for i in range (len(b)):
    if b in a:
        print("yes")
        break
    else:
        b=b[1:]+b[0]
else:
    print("no")