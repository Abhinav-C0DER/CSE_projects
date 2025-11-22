def prime_factors(n):
    n0=n
    res=[]
    i=2
    while i*i<=n:
        while n%i==0:
            res.append(i)
            n//=i
        i+=1
    if n>1:
        res.append(n)
    print(res)

n=int(input("Enter number: "))
prime_factors(n)