def is_prime(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        print(False)
        return
    m=(2**p)-1
    print(is_prime(m))

p=int(input("Enter prime p: "))
is_mersenne_prime(p)