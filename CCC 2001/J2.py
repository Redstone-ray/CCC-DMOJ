import sys
# import sympy
input = sys.stdin.readline
a,b = int(input()),int(input())
# try:
#     print(sympy.mod_inverse(a, b))
# except ValueError:
#     print("No such integer exists.")
InverseMod = lambda A, n,s=1,t=0,N=0: (n < 2 and t%N or InverseMod(n, A%n, t, s-A//n*t, N or n),"No such integer exists.")[n<1]
print(InverseMod(a,b))
