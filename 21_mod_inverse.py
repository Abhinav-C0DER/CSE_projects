def egcd(a,b):
    if b==0:
        return (1,0,a)
    x,y,g=egcd(b,a%b)
    return (y, x-(a//b)*y, g)

def mod_inverse(a,m):
    x,y,g=egcd(a,m)
    if g!=1:
        print(None)
    else:
        inv=x%m
        print(inv)

a=int(input("Enter a: "))
m=int(input("Enter m: "))
mod_inverse(a,m)