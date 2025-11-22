def count_divisors(n):
    cnt=0
    i=1
    while i*i<=n:
        if n%i==0:
            cnt+=1
            if i!=n//i:
                cnt+=1
        i+=1
    print(cnt)

n=int(input("Enter number: "))
count_divisors(n)