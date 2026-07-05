def Odd(No):
    return No % 2 != 0

def main():

    Data = [23,45,22,21,89,66]
    print("Input in Data is:",Data)

    FData = list(filter(Odd,Data))
    print("Odd Number is",FData)

if __name__ == "__main__":
    main()
    
