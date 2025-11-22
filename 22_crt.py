def crt(remainders, moduli):
    x=0
    M=1
    for m in moduli:
        M*=m
    for r,m in zip(remainders,moduli):
        Mi=M//m
        # find inverse of Mi mod m
        t=1
        while (Mi*t)%m!=1:
            t+=1
        x+=r*Mi*t
    print(x%M)

r=list(map(int,input("Enter remainders space separated: ").split()))
m=list(map(int,input("Enter moduli space separated: ").split()))
crt(r,m)