Min = lambda no1,no2: no1 if no1 < no2 else no2

value1 = int(input("Enter First number:"))
value2 = int(input("Enter second number:"))

print("Minimum Number is",Min(value1,value2))