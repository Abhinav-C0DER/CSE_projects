def mod_exp(base,exponent,modulus):
    result=1
    base=base%modulus
    while exponent>0:
        if exponent%2==1:
            result=(result*base)%modulus
        exponent//=2
        base=(base*base)%modulus
    return result

b=int(input("Enter base: "))
e=int(input("Enter exponent: "))
m=int(input("Enter modulus: "))
print(mod_exp(b,e,m))