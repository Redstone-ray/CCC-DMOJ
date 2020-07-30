moves = {54: 19, 90: 48, 99: 77, 9: 34, 40: 64, 67: 86}

pos = 1
n = int(input())
while n != 0:
    if pos + n <= 100:
        pos = moves.get(pos + n, pos + n)
    print('You are now on square',pos)
    if pos == 100:
        break
    n = int(input())
print('You Quit!' if n == 0 else 'You Win!')