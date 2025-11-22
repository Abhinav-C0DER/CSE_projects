def is_harshad(n):
    if n==0:
        print(False)
    else:
        s=0
        t=abs(n)
        while t>0:
            s+=t%10
            t//=10
        print(n % s == 0)

n=int(input("Enter number: "))
is_harshad(n)