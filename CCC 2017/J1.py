a=float(input())
time=0
count7=0
totalcount=0
while time<=a:
    if count7==6:
        count7=0
        time=time-1
    count7=count7+1
    totalcount=totalcount+1
    time=time+0.5
print(totalcount)