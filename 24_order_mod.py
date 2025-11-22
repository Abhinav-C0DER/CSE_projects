def order_mod(a,n):
    k=1
    val=a%n
    while val!=1:
        val=(val*a)%n
        k+=1
    print(k)

a=int(input("Enter a: "))
n=int(input("Enter n: "))
order_mod(a,n)