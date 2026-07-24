# Write a PYTHON program to print odd numbers up to n

n = int(input("Enter a number till where you want to print odd numbers: "))

for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
