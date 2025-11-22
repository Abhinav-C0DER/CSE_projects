def aliquot_sum(n):
    s=0
    i=1
    while i<n:
        if n%i==0:
            s+=i
        i+=1
    return s

def are_amicable(a,b):
    print(aliquot_sum(a)==b and aliquot_sum(b)==a)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
are_amicable(a,b)