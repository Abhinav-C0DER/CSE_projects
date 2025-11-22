def digital_root(n):
    n=abs(n)
    while n>9:
        s=0
        while n>0:
            s+=n%10
            n//=10
        n=s
    return n

n=int(input("Enter number: "))
print(digital_root(n))