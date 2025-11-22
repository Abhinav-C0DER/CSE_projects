import time
start=time.time()
def power(a,b,m):
    r=1
    for _ in range(b):
        r=(r*a)%m
    return r

def is_prime_miller_rabin(n,k):
    if n<2:
        return False
    d=n-1
    s=0
    while d%2==0:
        d//=2
        s+=1
    for i in range(k):
        a=2+(i%(n-3))
        x=power(a,d,n)
        if x==1 or x==n-1:
            continue
        ok=False
        for _ in range(s-1):
            x=(x*x)%n
            if x==n-1:
                ok=True
                break
        if not ok:
            return False
    return True

n=int(input())
k=int(input())
print(is_prime_miller_rabin(n,k))
end=time.time()
print("Time:",end-start)