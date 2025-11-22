def mean_of_digits(n):
    s=str(abs(n))
    total=0
    for ch in s:
        total += int(ch)
    return total/len(s)

n=int(input("Enter number: "))
print(mean_of_digits(n))