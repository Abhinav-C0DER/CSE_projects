def count_divisors(n):
    cnt=0
    i=1
    while i*i<=n:
        if n%i==0:
            cnt+=1
            if i!=n//i:
                cnt+=1
        i+=1
    return cnt

def is_highly_composite(n):
    d=count_divisors(n)
    i=1
    while i<n:
        if count_divisors(i)>=d:
            print(False)
            return
        i+=1
    print(True)

n=int(input("Enter number: "))
is_highly_composite(n)