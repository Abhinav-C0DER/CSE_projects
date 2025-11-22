def is_prime(n):
    if n<2:
        return False
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True

def is_fibonacci(n):
    if n==0:
        return True
    a,b=0,1
    while b<=n:
        if b==n:
            return True
        a,b=b,a+b
    return False

def is_fibonacci_prime(n):
    print(is_prime(n) and is_fibonacci(n))

n=int(input("Enter number: "))
is_fibonacci_prime(n)