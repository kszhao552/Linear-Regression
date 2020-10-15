def updateVals(entriesList):
    for i in range(len(entriesList)):
        entriesList[i] = int(input())

def average(list):
    avg = 0
    for i in range(len(list)):
        avg += list[i]

    avg /= len(list)
    return avg

def sumSquare(list1, list2):
    sum1 = 0
    sumx = 0
    sumy = 0

    for i in range(len(list1)):
        sum1 += list1[i]*list2[i]
        sumx += list1[i]
        sumy += list2[i]

    sum2 = sumx*sumy
    sum2 /= len(list1)

    return sum1 - (sum2)

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
    
    print('\n')
    print(f'xbar = {xbar}')
    print(f'ybar = {ybar}')
    
    SSxx = sumSquare(x, x)
    SSyy = sumSquare(y, y)
    SSxy = sumSquare(x, y)

    print('\n')
    print(f'SSxx = {SSxx}')
    print(f'SSyy = {SSyy}')
    print(f'SSxy = {SSxy}')
    

