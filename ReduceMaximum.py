from functools import reduce

def main():

    Data = [12,34,67,98,90]
    print("Input Data is:",Data)

    RData = reduce(lambda no1,no2: no1 if no1 > no2 else no2,Data)
    print("Maximum number is",RData)

if __name__ == "__main__":
    main()