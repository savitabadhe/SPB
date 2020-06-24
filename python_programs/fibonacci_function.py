
def FibRecursion(n):
    if n <= 1:
        return n
    else:
        return (FibRecursion(n - 1) + FibRecursion(n - 2))


value = int(input("Enter the value till you want fibonacci series? "))

if value <= 0:  # check if the number is valid
    print("Please enter a positive integer")
else:
    print("Fibonacci series is:")
    for i in range(value):
        print(FibRecursion(i))
