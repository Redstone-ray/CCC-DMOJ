a = int(input())
b = int(input())
if b <= a:
    print("Congratulations, you are within the speed limit!")

else:
    c=b-a
    if c <= 20:
        print("You are speeding and your fine is $100.")
    elif c<=30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")
