import time
start=time.time()
def collatz_length(n):
    c=0
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        c+=1
    return c

n=int(input())
print(collatz_length(n))
end=time.time()
print("Time:",end-start)