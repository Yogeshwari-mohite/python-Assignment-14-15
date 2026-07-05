def Square(No):
    return No * No

def main():

    Data = [2,4,5,6,2]
    print("Input Data is:",Data)

    MData = list(map(Square,Data))
    print("Square number is",MData)

if __name__ == "__main__":
    main()
