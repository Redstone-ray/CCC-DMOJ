'''
Loop through each char
if phrase, yes, break
else, move last char to first, loop
'''
a=input()
b=input()
for i in range (len(b)):
    if b in a:
        print("yes")
        break
    else:
        b=b[1:]+b[0]
else:
    print("no")
