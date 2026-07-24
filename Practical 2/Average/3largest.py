"""
Write a PYTHON program to find largest of three numbers.
"""

n1, n2, n3 = int(input("Enter first number : ")), int(input("Enter second number : ")), int(input("Enter third number : "))

if (n1 > n2):
    if n1 > n3:
        print(f"{n1} is largest")
    else:
        print(f"{n3} is largest")
else:
    if n2 > n3:
        print(f"{n2} is largest")
    else:
        print(f"{n3} is largest")


