import time
start=time.time()
def f(x,n):
    return (x*x+1)%n

def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def pollard_rho(n):
    if n%2==0:
        return 2
    x=2
    y=2
    d=1
    while d==1:
        x=f(x,n)
        y=f(f(y,n),n)
        d=gcd(abs(x-y),n)
    if d==n:
        return None
    return d

n=int(input())
print(pollard_rho(n))
end=time.time()
print("Time:",end-start)