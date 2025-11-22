import time
start=time.time()
def power(a,b,m):
    r=1
    for _ in range(b):
        r=(r*a)%m
    return r

def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x

def is_carmichael(n):
    for a in range(2,n):
        if gcd(a,n)==1:
            if power(a,n-1,n)!=1:
                return False
    return True

n=int(input())
print(is_carmichael(n))
end=time.time()
print("Time:",end-start)