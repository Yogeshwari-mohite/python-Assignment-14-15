Grater = lambda x, y, z: x if x > y and x > z else ( y  if  y > z else z)

a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))

Ret = Grater(a,b,c)

print("Greater number is:",Ret)