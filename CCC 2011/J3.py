'''
128 71
        49
            22
                27
                    -5
'''

cases = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
n = int(input())
eliminated = set()
for i in range(n):
    eliminated.add(int(input()) - 1)
offer = int(input())
avg = 0
for i in range(len(cases)):
    if i not in eliminated:
        avg += cases[i]
avg /= (len(cases) - n)
print('deal' if offer > avg else 'no deal')
