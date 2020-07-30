y=int(input())
while True:
    y+=1
    for i in range(len(str(y))):
        d=str(y)[i]
        if str(y).count(d)>1:
            break
    else:
        print(y)
        break