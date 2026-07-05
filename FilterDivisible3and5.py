numbers = [10,20,30,40,50,60,75]

FData = list(filter(lambda x: x % 3 == 0 and x % 5 == 0,numbers))

print(FData)