nikkyForward=int(input())
nikkyBackward=int(input())

byronForward=int(input())
byronBackward=int(input())
total=int(input())

def walk(forward,backward):
    steps=0
    currsteps=0
    while True:
        for i in range(forward):
            steps+=1
            currsteps+=1
            if currsteps >= total:
                return steps

        for i in range(backward):
            steps-=1
            currsteps+=1
            if currsteps >= total:
                return steps
ns=walk(nikkyForward,nikkyBackward)
bs=walk(byronForward,byronBackward)
if ns>bs:
    print("Nikky")
elif bs>ns:
    print("Byron")
else:
    print("Tied")