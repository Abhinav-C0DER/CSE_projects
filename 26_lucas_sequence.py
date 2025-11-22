import time
start=time.time()

def lucas(n):
    if n==0:
        return 2
    if n==1:
        return 1
    return lucas(n-1)+lucas(n-2)

n=int(input())
for i in range(n):
    print(lucas(i),end=" ")

end=time.time()
print("\nTime:",end-start)