a,b=int(input()),int(input())

if a+b<10:
    print("There are 0 ways to get the sum 10.")
elif a+b==10:
    print("There is 1 way to get the sum 10.")
else:
    for i in range(1,10):
        count = 0
        if a >= i and b >= (10 - i):
            count += 1
    print('There are ' + str(count) + ' ways to get the sum 10.')