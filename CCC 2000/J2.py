def isSameAfterRotate180(num):
   l=list(str(num))
   for i,c in enumerate(l):
       if c=='6':
           l[i]='9'
       elif c=='9':
           l[i]='6'
       elif c in '23457':
           return False

   if num==int(''.join(reversed(l))):
       return True
   else:
       return False

a=int(input())
b=int(input())

count=0
for n in range(a,b+1):
   if isSameAfterRotate180(n):
       count+=1
print(count)
