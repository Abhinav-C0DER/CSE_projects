def count_distinct_prime_factors(n):
    count=0
    i=2
    temp=n
    while i*i<=temp:
        if temp%i==0:
            count+=1
            while temp%i==0:
                temp//=i
        i+=1
    if temp>1:
        count+=1
    print(count)

n=int(input("Enter number: "))
count_distinct_prime_factors(n)