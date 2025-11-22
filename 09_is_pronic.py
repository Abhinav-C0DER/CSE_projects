def is_pronic(n):
    if n<0:
        print(False)
    else:
        i=0
        while i*(i+1)<=n:
            if i*(i+1)==n:
                print(True)
                return
            i+=1
        print(False)

n=int(input("Enter number: "))
is_pronic(n)