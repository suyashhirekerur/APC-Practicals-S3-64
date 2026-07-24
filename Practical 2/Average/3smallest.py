# Write a PYTHON program to find smallest of three numbers

n1, n2, n3 = int(input("Enter first number : ")), int(input("Enter second number : ")), int(input("Enter third number : "))

if (n1 < n2):
    if n1 < n3:
        print(f"{n1} is smallest")
    else:
        print(f"{n3} is smallest")
else:
    if n2 < n3:
        print(f"{n2} is smallest")
    else:
        print(f"{n3} is smallest")