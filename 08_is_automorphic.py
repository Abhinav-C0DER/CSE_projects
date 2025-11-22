def is_automorphic(n):
    sq=n*n
    print(str(sq).endswith(str(n)))

n=int(input("Enter number: "))
is_automorphic(n)