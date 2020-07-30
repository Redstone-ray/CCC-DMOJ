a=input()
happy = 0
sad = 0
for i in range(len(a)):
    if a[i:i+3] == ":-)":
        happy += 1
    elif a[i:i+3] == ":-(":
        sad += 1
if happy > sad:
    print('happy')
elif happy == sad !=0:
    print('unsure')
elif sad > happy:
    print('sad')
else:
    print('none')