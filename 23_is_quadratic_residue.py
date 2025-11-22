def is_quadratic_residue(a,p):
    a=a%p
    found=False
    x=0
    while x<p:
        if (x*x)%p==a:
            found=True
            break
        x+=1
    print(found)

a=int(input("Enter a: "))
p=int(input("Enter prime p: "))
is_quadratic_residue(a,p)