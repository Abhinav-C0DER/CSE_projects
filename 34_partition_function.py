import time
start=time.time()
def partition_function(n):
    dp=[0]*(n+1)
    dp[0]=1
    for i in range(1,n+1):
        for j in range(i,n+1):
            dp[j]+=dp[j-i]
    return dp[n]

n=int(input())
print(partition_function(n))
end=time.time()
print("Time:",end-start)