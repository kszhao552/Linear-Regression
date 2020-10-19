from vector import Vector
from regression import LinearRegression
import math


def sumSquare(vector1, vector2):
    """calcultes the sum of the squares for two vectors through the formula
    summation(v1i*v2i) - sumation(v1i)*summation(v2i)/n"""

    #calculate the first summation of the equation
    sum1 = 0
    for i in range(vector1.size):
        sum1 += vector1.data[i] * vector2.data[i]

    #calculate the second summation of the equation
    sum2 = vector1.average*vector2.average
    sum2 *= vector1.size

    #return the difference between the two/
    return sum1 - (sum2)

if __name__ == "__main__":
    """TODO: calculate the f statistic and change the print statements to write to a new file output
    Round the variables to 3 decimal places as well"""

    #initalize the x and y vectors with the proper sizes.
    numEntries = int(input("How many entries in the database: "))
    x = Vector(numEntries)
    y = Vector(numEntries)


    print("Please input the x values")
    x.updateVals() #get the values for the x vector

    print("Please input the y values (with respect to the x values)")
    y.updateVals() #get the values for the y vector

    #prints out the vectors for easier reading
    print('\n')
    print(f'The x vector is {x.data}')
    print(f'The y vector is {y.data}')

    #prints out the averages of the two vectors
    print('\n')
    print(f'xbar = {x.average}')
    print(f'ybar = {y.average}')
   
    #Creates a linear regression class with the size of input given at the start of the program
    line = LinearRegression(numEntries)
    line.SSxx = sumSquare(x, x) #calculates sum((xi-xbar)^2)
    line.SSyy = sumSquare(y, y) #calculates sum((yi - ybar)^2)
    line.SSxy = sumSquare(x, y) #calculates sum((xi - xbar)(yi-ybar))

    #prints out the values that were just calculated
    print('\n')
    print(f'SSxx = {line.SSxx}')
    print(f'SSyy = {line.SSyy}')
    print(f'SSxy = {line.SSxy}')
   
    
    line.update_vals(x, y) #creates the values for the linear regression.
    errors = line.errorList(x.data, y.data) #creates the vector of the errors of the linear regression
    line.rSquared = line.SSxy/(math.sqrt(line.SSxx*line.SSyy)) #calculates the coefficient of determination
    line.r = math.sqrt(line.rSquared) #calculates the coefficient of correlation

    #prints out the values that the script just calculated
    print("\n")
    print(f'the regression is yhat = {line.bhat0} + {line.bhat1}x')
    print(f'r² = {line.rSquared}')
    print(f'r = {line.r}')
    print(f'the vector of errors is {errors.data}')
    
    #Calclates the analysis of variance for the regression
    #i.e Error Sum of Squares, Regression Sum of Square, and Total Sum of Squares
    line.SSE = sumSquare(errors, errors)
    line.SSTO = sumSquare(y, y)
    line.SSR = line.SSTO - line.SSE
    #prints out the values that was just calculated
    print('\n')
    print(f'SSTO = {line.SSTO}')
    print(f'SSE = {line.SSE}')
    print(f'SSR = {line.SSR} = MSR')

    #Calculates the variance and the standard deviation of the linear regression
    line.var = line.SSE/(line.size-2)
    line.sd = math.sqrt(line.var)
    print('\n')
    print(f'var = {line.var} = MSE')
    print(f'sd = {line.sd} = MSRE')


    

    