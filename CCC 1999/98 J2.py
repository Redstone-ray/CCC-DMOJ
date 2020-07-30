for n in range(1000,9999+1):
    divisors=[]
    for d in range(1,int(n**.5)+1):
        if n%d==0:
            divisors.append(d)
            divisors.append(n//d)
    if sum(divisors)==n:
        print(n,end=" ")