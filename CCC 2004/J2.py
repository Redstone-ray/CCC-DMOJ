a=int(input())
b=int(input())
c=b-a
mayor=0
tre=0
chief=0
dog=0
print("All positions change in year",a)
for i in range (c):
    mayor=mayor+1
    tre=tre+1
    chief=chief+1
    dog=dog+1
    a=a+1
    if mayor == 4:
        mayor=0
    if tre == 2:
        tre=0
    if chief == 3:
        chief=0
    if dog ==5:
        dog=0
    if mayor ==0 and tre==0 and chief ==0 and dog ==0:
        print("All positions change in year",a)