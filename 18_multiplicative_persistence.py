def multiplicative_persistence(n):
    c=0
    while n>9:
        prod=1
        t=abs(n)
        while t>0:
            prod*=t%10
            t//=10
        n=prod
        c+=1
    print(c)

n=int(input("Enter number: "))
multiplicative_persistence(n)