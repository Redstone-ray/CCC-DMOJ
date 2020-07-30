import sys
input = sys.stdin.readline

begin, days = map(int, input().split())
begin -= 1
count= 1
#Go directly to the day of the week (day 1)
print("Sun Mon Tue Wed Thr Fri Sat")
for i in range(begin):
    print('    ', end='')
while True:
    print('%3d' % (count), end='')
    if count == days:
        print()
        break
    count += 1
    begin += 1
    #switch to a new line
    if begin == 7:
        begin = 0
        print()
    else:
        print(" ", end='')
