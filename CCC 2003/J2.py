import sys
import math

input = sys.stdin.readline
# first take in a area
a = int(input())
while a != 0:
    # Get the side length
    sqrtA = int(math.sqrt(a))
    while a % sqrtA != 0:
        sqrtA -= 1
    w = int(a / sqrtA)
    print('Minimum perimeter is',(2 * (sqrtA + w)),'with dimensions',sqrtA,'x',w)
    a = int(input())
