n=int(input())
for i in range(n):
    num=int(input())
    backup=num
    print(num)

    while num>100:
        last_digit=num%10
        num=num//10
        num=num-last_digit
        print(num)
    print("The number",backup,"is divisible by 11.")