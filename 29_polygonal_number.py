import time
start=time.time()
def polygonal_number(s,n):
    return ((s-2)*n*n-(s-4)*n)//2

s=int(input())
n=int(input())
print(polygonal_number(s,n))
end=time.time()
print("Time:",end-start)