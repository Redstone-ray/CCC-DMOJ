d = int(input())
e = int(input())
w = int(input())

if d > 100:
    a = (d - 100)*25 + 15*e + 20*w
else:
    a = 15*e + 20*w

if d > 250:
    b = (d - 250)*45 + 35*e + 25*w
else:
    b = 35*e + 25*w

print(f'Plan A costs {a/100}')
print(f'Plan B costs {b/100}')

if a > b:
    print('Plan B is cheapest.')
elif a == b:
    print('Plan A and B are the same price.')
elif a < b:
    print('Plan A is cheapest.')
