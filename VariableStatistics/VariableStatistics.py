from vector import Vector
from regression import LinearRegression

def sumSquare(vector1, vector2):
    sum1 = 0

    for i in range(vector1.size):
        sum1 += vector1.data[i] * vector2.data[i]


    sum2 = vector1.average*vector2.average
    sum2 *= vector1.size

    return sum1 - (sum2)

if __name__ == "__main__":
    numEntries = int(input("How many entries in the database: "))
    x = Vector(numEntries)
    y = Vector(numEntries)

    print("Please input the x values")
    x.updateVals()

    print("Please input the y values (with respect to the x values)")
    y.updateVals()

    
    print('\n')
    print(f'xbar = {x.average}')
    print(f'ybar = {y.average}')
   
    line = LinearRegression(numEntries)
    line.SSxx = sumSquare(x, x)
    line.SSyy = sumSquare(y, y)
    line.SSxy = sumSquare(x, y)

    print('\n')
    print(f'SSxx = {line.SSxx}')
    print(f'SSyy = {line.SSyy}')
    print(f'SSxy = {line.SSxy}')

    line.update_vals(x, y)
    errors = line.errorList(x, y)

    print(f'the regression is yhat = {line.bhat0} + {line.bhat1}x')
    print(f'the vector of errors is {line.errors}')
    

    