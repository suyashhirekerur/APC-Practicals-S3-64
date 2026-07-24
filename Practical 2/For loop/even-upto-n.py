# Write a PYTHON program to print even numbers up to n.

n = int(input("Enter a number till where you want to print even numbers: "))

for i in range(1, n):
    if i % 2 == 0:
        print(i, end=" ")