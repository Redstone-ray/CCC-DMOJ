a=int(input())
for i in range(a):
    d = {}
    count = 0
    while True:
        b=input()
        if not b:
            break
        for i in b.split():
            if i not in d:
                count+=1
                d[i]=count
                print(i,end=" ")
            else:
                print(d[i],end=" ")
        print()
'''
2
the cat chased the rat while
the dog chased the cat into the rat housethe cat chased the rat while
the dog chased the cat into the rat housethe cat chased the rat while
the dog chased the cat into the rat house
'''