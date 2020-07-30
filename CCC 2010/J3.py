a=0
b=0
while True:
   c = input().split()
   if c[0] == '1':
       if c[1]=='A':
           exec('a=int(c[2])')
       else:
           exec('b=int(c[2])')
   elif c[0] == '2':
       if c[1]=='A':
           exec('print(a)')
       else:
           exec('print(b)')
   elif c[0] == '3':
       if c[1] == 'A' and c[2] != 'A':
           exec('a=a+b')
       elif c[1] == 'A' and c[2] == 'A':
           exec('a=a+a')
       elif c[2] == 'B':
           exec('a=b+b')
       else:
           exec('b=a+b')
   elif c[0] == '4':
       if c[1] == 'A' and c[2]!='A':
           exec('a=a*b')
       elif c[1] == 'A' and c[2] == 'A':
           exec('a=a*a')
       elif c[2] == 'B':
           exec('a=b*b')
       else:
           exec('b=a*b')
   elif c[0] == '5':
       if c[1] == 'A' and c[2] != 'A':
           exec('a=a-b')
       elif c[1] == 'A' and c[2] == 'A':
           exec('a=a-a')
       elif c[2] == 'B':
           exec('a=b-b')
       else:
           exec('b=b-a')
   elif c[0] == '6':
       if c[1] == 'A' and c[2] != 'A':
           exec('a=a//b')
       elif c[1] == 'A' and c[2] == 'A':
           exec('a=a//a')
       elif c[2] == 'B':
           exec('a=b//b')
       else:
           exec('b=b//a')
   else:
       break
