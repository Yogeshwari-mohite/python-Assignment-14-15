from functools import reduce

def Add(no1,no2):
    return no1 + no2

def main():

    Data = [12,22,44,33]
    print("Input Data is :",Data)

    RData = reduce(Add,Data)
    print("Addition is",RData)

if __name__ == "__main__":
    main()