def is_deficient(n):
    if n<1:
        print(False)
    else:
        s=0
        i=1
        while i<n:
            if n%i==0:
                s+=i
            i+=1
        print(s<n)

n=int(input("Enter number: "))
is_deficient(n)