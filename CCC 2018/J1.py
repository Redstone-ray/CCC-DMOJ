first=int(input())
second=int(input())
third=int(input())
forth=int(input())
if second == third:
    if first == 0 or first == 9:
        if forth == 8 or forth == 9:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")