def aliquot_sum(n):
    s=0
    i=1
    while i<n:
        if n%i==0:
            s+=i
        i+=1
    print(s)

n=int(input("Enter number: "))
aliquot_sum(n)