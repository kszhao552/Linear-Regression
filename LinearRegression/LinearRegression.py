from vector import Vector
from regression import LinearRegression
import math
import csv
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

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

def initializeVectors(x, y):
     #ask the user to select a file path.
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename()

    with open(filePath, 'r') as input_file:
        csv_reader = csv.reader(input_file, delimiter=',')

        #Use a sniffer to see if there is a header
        sniffer = csv.Sniffer()
        header = sniffer.has_header(input_file.read(32))

        #get the length of the csv file
        lines= len(list(csv_reader))

        #if there is a header, then we move to the next line, and remove it from our line count
        if header:
            next(csv_reader)
            lines -= 1

        #update the length of the vectors to match the data set.
        x.updateLen(lines)
        y.updateLen(lines)



def inputManual(x, y):
        #file was not a csv and we need to get manual input
        #initalize the x and y vectors with the proper sizes.
        print("File is not a csv file. Please input the data manually.")
        numEntries = int(input("How many entries in the database: "))
        x = Vector(numEntries)
        y = Vector(numEntries)


        print("Please input the x values")
        x.updateVals() #get the values for the x vector

        print("Please input the y values (with respect to the x values)")
        y.updateVals() #get the values for the y vector


if __name__ == "__main__":
    """TODO: Take in csv file as input for larger data sets."""
    x = Vector(0)
    y = Vector(0)
    initializeVectors(x, y)

    file = open("output.txt", "w")

    #prints out the vectors for easier reading
    file.write(f'The x vector is {x.data}\n')
    file.write(f'The y vector is {y.data}\n')

    #prints out the averages of the two vectors
    file.write('\n')
    file.write(f'xbar = {x.average}\n')
    file.write(f'ybar = {y.average}\n')
   
    #Creates a linear regression class with the size of input given at the start of the program
    line = LinearRegression(numEntries)
    line.SSxx = round(sumSquare(x, x), 3) #calculates sum((xi-xbar)^2)
    line.SSyy = round(sumSquare(y, y), 3) #calculates sum((yi - ybar)^2)
    line.SSxy = round(sumSquare(x, y), 3) #calculates sum((xi - xbar)(yi-ybar))

    #prints out the values that were just calculated
    file.write('\n')
    file.write(f'SSxx = {line.SSxx}\n')
    file.write(f'SSyy = {line.SSyy}\n')
    file.write(f'SSxy = {line.SSxy}\n')
   
    
    line.update_vals(x, y) #creates the values for the linear regression.
    errors = line.errorList(x.data, y.data) #creates the vector of the errors of the linear regression
    line.rSquared = round(abs(line.SSxy/(math.sqrt(line.SSxx*line.SSyy))), 3) #calculates the coefficient of determination
    line.r = round(math.sqrt(line.rSquared), 3) #calculates the coefficient of correlation
    if(line.bhat1 < 0): # if the slope is negative, then we need to make r negative.
        line.r *= -1
    yhat = line.yhatList(x.data)

    #prints out the values that the script just calculated
    file.write("\n")
    file.write(f'the regression is yhat = {line.bhat0} + {line.bhat1}x\n')
    file.write(f'r² = {line.rSquared}\n')
    file.write(f'r = {line.r}\n')
    file.write(f'the vector of the predicted values is {yhat.data}\n')
    file.write(f'the vector of errors is {errors.data}\n')
    
    #Calclates the analysis of variance for the regression
    #i.e Error Sum of Squares, Regression Sum of Square, and Total Sum of Squares
    line.SSE = round(sumSquare(errors, errors), 4)
    line.SSTO = round(sumSquare(y, y), 4)
    line.SSR = round(line.SSTO - line.SSE, 4)
    #prints out the values that was just calculated
    file.write('\n')
    file.write(f'SSTO = {line.SSTO}\n')
    file.write(f'SSE = {line.SSE}\n')
    file.write(f'SSR = {line.SSR} = MSR\n')

    #Calculates the variance and the standard deviation of the linear regression
    line.var = round(line.SSE/(line.size-2), 3)
    line.sd = round(math.sqrt(line.var), 3)
    file.write('\n')
    file.write(f'var = {line.var} = MSE\n')
    file.write(f'sd = {line.sd} = MSRE\n')

    #Calculate the f statistic and return it with proper amount of df
    line.fStat()
    file.write('\n')
    file.write(f'f = {line.f} with (1, {line.size-2}) degrees of freedom\n')
    file.close()

    #writes the vectors into a csv file for a later reference
    with open('vectors.csv', mode = 'w', newline='') as vector_file:
        vector_writer = csv.writer(vector_file, delimiter = ',', quotechar = '"',quoting = csv.QUOTE_MINIMAL)
        
        vector_writer.writerow(['x', 'y', 'yhat', 'errors'])
        for i in range(numEntries):
            vector_writer.writerow([x.data[i], y.data[i], yhat.data[i], errors.data[i]])
    
    print('\n')
    print(f'Output has been created in the directory')
