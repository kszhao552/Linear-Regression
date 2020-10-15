def updateVals(entriesList):
    for i in range(len(entriesList)):
        entriesList[i] = int(input())

def average(list):
    avg = 0
    for i in range(len(list)):
        avg += list[i]

    avg /= len(list)
    return avg

if __name__ == "__main__":
    numEntries = int(input("How many entries in the database: "))
    x = [0 for i in range(numEntries)]
    y = [0 for i in range(numEntries)]

    print("Please input the x values")
    updateVals(x)

    print("Please input the y values (with respect to the x values)")
    updateVals(y)

    xbar = average(x)
    ybar = average(y)
    print(xbar)
    print(ybar)

