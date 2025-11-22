def is_prime(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def twin_primes(limit):
    res=[]
    prev=2
    i=3
    while i<=limit:
        if is_prime(i):
            if i-prev==2:
                res.append((prev,i))
            prev=i
        i+=1
    return res

n=int(input("Enter limit: "))
print(twin_primes(n))