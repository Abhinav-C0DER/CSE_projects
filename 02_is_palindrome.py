def is_palindrome(n):
    s=str(n)
    return s==s[::-1]

n=int(input("Enter number: "))
print(is_palindrome(n))