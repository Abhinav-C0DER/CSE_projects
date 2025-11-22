import time
start=time.time()
def is_perfect_power(n):
    for a in range(2,n):
        p=a*a
        while p<=n:
            if p==n:
                return True
            p=p*a
    return False

n=int(input())
print(is_perfect_power(n))
end=time.time()
print("Time:",end-start)