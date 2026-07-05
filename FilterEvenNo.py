def Even(No):
    return No % 2 == 0


def main():

    Data = [2,3,4,5,6,7]
    print("Input Data is:",Data)

    FData = list(filter(Even,Data))
    print("Even Number is",FData)

if __name__ == "__main__":
    main()