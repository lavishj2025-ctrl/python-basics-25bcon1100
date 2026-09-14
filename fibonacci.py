n = int(input("Enter number of terms: "))
first = 0
second = 1
print("Fibonacci series:", end="")
for i in range(1, n + 1):
    print(f"{first},", end="")
    next_term = first + second
    first = second
    second = next_term
print()