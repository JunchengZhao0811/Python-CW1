from NumberList import NumberList
import sys

def mean(data):
    return sum(data) / len(data) if data else None

def variance(data):
    if not data or len(data) < 2:
        return None
    data_mean = mean(data)
    return sum((x - data_mean) ** 2 for x in data) / (len(data) - 1)

def main():
    nlist = NumberList()
    nargs = len(sys.argv)

    if nargs == 1:
        nlist.getDataFromKeyboard()
    elif nargs == 2:
        nlist.getDataFromFile(sys.argv[1])
    elif nargs in (3, 4):
        args = sys.argv[1:]
        nlist.getRandomData(*args)
    else:
        print("Incorrect number of arguments, try again")
        sys.exit()

    data = nlist.getData()
    print(f"Numbers: {data}")
    print(f"Mean: {mean(data)}")
    print(f"Variance: {variance(data)}")

if __name__ == "__main__":
    main()
