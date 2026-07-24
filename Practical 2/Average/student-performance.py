"""
Write a PYTHON program to evaluate the student
performance
If % is >=90 then Excellent performance
If % is >=80 then Very Good performance
If % is >=70 then Good performance
If % is >=60 then average performance
else Poor performance.
"""

per = float(input("Enter your percentage: "))

if per >=90 and per <=100:
    print("Excellent Performance")
elif per>=80 and per <90:
    print("Very good performance")
elif per>=70 and per <80:
    print("Good performance")
elif per >=60 and per<70:
    print("Average performance")
else:
    print("Poor performance")

