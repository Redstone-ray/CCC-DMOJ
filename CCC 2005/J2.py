low,high = int(input()),int(input())

count = 0
for x in range(low, high + 1):
    countDivisors = 0
    for y in range(1, x + 1):
        #if reminder is 0
        if x % y == 0:
            countDivisors += 1
        # if there are four divisors break
            if countDivisors > 4:
                break
        #If there are exactly 4 divisors
    if countDivisors == 4:
        #Add one to RSA numbers count
        count += 1
print('The number of RSA numbers between ',low,' and ',high,+ ' is ',count)