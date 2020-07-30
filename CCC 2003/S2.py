# a,e,i,o,u

syl = ["a", "e", "i", "o", "u"]
a = int(input())
for i in range(a):
    l = []
    b = input().split()[-1]
    c = input().split()[-1]
    d = input().split()[-1]
    e = input().split()[-1]

# One plus one is small
# one hundred plus one is not
# you might be very tall
# but summer is not
    if b==c==d==e:
        print("perfect")
    elif b==c and d==e:
        print("even")
    elif b==e and c==d:
        print("shell")
    elif b==d and c==e:
        print("cross")
    else:
        print("free")

