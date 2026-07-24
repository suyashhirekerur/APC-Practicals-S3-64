# Write a PYTHON program that prints 1 2 4 8 16 32 ... n2

n = int(input("Enter the number till where you want to print its doubled value: "))

for i in range(0, n):
    n *= 2
    print(n)

    