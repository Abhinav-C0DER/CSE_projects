def is_prime(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def is_prime_power(n):
    if n<=1:
        print(False)
        return
    i=2
    while i*i<=n:
        if is_prime(i):
            p=i
            val=p*p
            while val<=n:
                if val==n:
                    print(True)
                    return
                val*=p
        i+=1
    if is_prime(n):
        print(True)
    else:
        print(False)

n=int(input("Enter number: "))
is_prime_power(n)