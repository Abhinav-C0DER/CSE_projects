import time
start=time.time()
def zeta_approx(s,t):
    total=0
    for n in range(1,t+1):
        p=1
        for _ in range(s):
            p=p*n
        total+=1/p
    return total

s=int(input())
terms=int(input())
print(zeta_approx(s,terms))
end=time.time()
print("Time:",end-start)