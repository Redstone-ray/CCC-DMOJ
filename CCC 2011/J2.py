h=int(input())
m=int(input())
import sys
for i in range (1,m):
    a=-6*(i**4)+h*(i**3)+2*(i**2)+i
    if a<=0:
        print("The balloon first touches ground at hour:")
        print(i)
        sys.exit(0)
print("The balloon does not touch ground in the given time.")