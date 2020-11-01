from vector import Vector
from regression import Regression
import math
import csv
import pandas
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
import sys
import traceback

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

def initializeVectors(x, y, filePath):
   


    with open(filePath, 'r+') as input_file:
        csv_reader = csv.reader(input_file, delimiter=',')
        
       

        #Use a sniffer to see if there is a header
        sniffer = csv.Sniffer()
        header = sniffer.has_header(input_file.read(32))
        input_file.seek(0)

        #get the length of the csv file
        lines= len(list(csv_reader))
        input_file.seek(0)
        #if there is a header, then we move to the next line, and remove it from our line count
        if header:
            next(csv_reader, None)
            lines -= 1
        if lines <3:
            raise ValueError(f"Error: Sample size not large enough")

        #update the length of the vectors to match the data set.
        x.updateLen(lines)
        y.updateLen(lines)

        #i will keep count of position in vector
        i = 0
        #goes through each rows in the csv file and updates x and y
        for row in csv_reader:
            try:
                x.data[i] = float(row[0])
                y.data[i] = float(row[1])
                i += 1
            except ValueError:
                raise ValueError(f'Contains non-number value')

        #updates the average of the vectors
        x.avg()
        y.avg()


def inputManual(x, y):
        #file was not a csv and we need to get manual input
        #initalize the x and y vectors with the proper sizes.
        try:
            numEntries = int(input(f"How many entries in the database: "))
        except ValueError:
            raise ValueError("Input is not number")
        if numEntries < 3:
            raise Exception(f"Error: Invalid Sample Size")
        x.updateLen(numEntries)
        y.updateLen(numEntries)


        print(f"Please input the x values")
        x.updateVals() #get the values for the x vector

        print(f"Please input the y values (with respect to the x values)")
        y.updateVals() #get the values for the y vector


def writeToFile(x, y, line, yhat, errors):     

        file = open("output.txt", "w")

        #prints out the vectors for easier reading
        file.write(f'The x vector is {x.data}\n')
        file.write(f'The y vector is {y.data}\n')

        #prints out the averages of the two vectors
        file.write('\n')
        file.write(f'xbar = {x.average}\n')
        file.write(f'ybar = {y.average}\n')
   
        #Creates a linear regression class with the size of input given at the start of the program
        

        #prints out the values that were just calculated
        file.write('\n')
        file.write(f'SSxx = {line.SSxx}\n')
        file.write(f'SSyy = {line.SSyy}\n')
        file.write(f'SSxy = {line.SSxy}\n')        

        #prints out the values that the script just calculated
        file.write("\n")
        file.write(f'the regression is yhat = {line.bhat0} + {line.bhat1}x\n')
        file.write(f'r² = {line.rSquared}\n')
        file.write(f'r = {line.r}\n')
        file.write(f'the vector of the predicted values is {yhat.data}\n')
        file.write(f'the vector of errors is {errors.data}\n')
    

        #prints out the values that was just calculated
        file.write('\n')
        file.write(f'SSTO = {line.SSTO}\n')
        file.write(f'SSE = {line.SSE}\n')
        file.write(f'SSR = {line.SSR} = MSR\n')

     
        file.write('\n')
        file.write(f'var = {line.var} = MSE\n')
        file.write(f'sd = {line.sd} = MSRE\n')

        #Calculate the f statistic and return it with proper amount of df
        file.write('\n')
        file.write(f'f = {line.f} with (1, {line.size-2}) degrees of freedom\n')
        file.close()

        #writes the vectors into a csv file for a later reference
        with open('vectors.csv', mode = 'w', newline='') as vector_file:
            vector_writer = csv.writer(vector_file, delimiter = ',', quotechar = '"',quoting = csv.QUOTE_MINIMAL)
        
            vector_writer.writerow(['x', 'y', 'yhat', 'errors'])
            for i in range(x.size):
                vector_writer.writerow([x.data[i], y.data[i], yhat.data[i], errors.data[i]])
    
        print('\n')

def calculateLine(x, y, line):
    line.updateLen(x.size)
    line.SSxx = round(sumSquare(x, x), 3) #calculates sum((xi-xbar)^2)
    line.SSyy = round(sumSquare(y, y), 3) #calculates sum((yi - ybar)^2)
    line.SSxy = round(sumSquare(x, y), 3) #calculates sum((xi - xbar)(yi-ybar))

    line.update_vals(x, y) #creates the values for the linear regression.

    if (line.SSxx == 0 or line.SSyy == 0):
        raise ZeroDivisionError("Regression is a flat line.")
    line.r = round(line.SSxy/(math.sqrt(line.SSxx*line.SSyy)), 3) #calculates the coefficient of determination
    line.rSquared = round(pow(line.r, 2), 3) #calculates the coefficient of correlation



def calculatePredicted(x, line):
    yhat = line.yhatList(x.data)
    return yhat
    
def calculateErrors(x, y, line, yhat, errors):
    errors = line.errorList(y.data, yhat.data) #creates the vector of the errors of the linear regression
    #Calclates the analysis of variance for the regression
    #i.e Error Sum of Squares, Regression Sum of Square, and Total Sum of Squares
    line.SSE = round(sumSquare(errors, errors), 4)
    line.SSTO = round(sumSquare(y, y), 4)
    line.SSR = round(line.SSTO - line.SSE, 4)

    #Calculates the variance and the standard deviation of the linear regression
    line.var = round(line.SSE/(line.size-2), 3)
    line.sd = round(math.sqrt(line.var), 3)

    line.fStat()

    return errors

def main():
    """TODO: Take in csv file as input for larger data sets."""
    x = Vector(0)
    y = Vector(0)
    line = Regression(0)
    errors = Vector(0)
    predicted = Vector(0)

    #ask the user to select a file path.
    root = tk.Tk()
    root.withdraw()
    filePath = filedialog.askopenfilename()

    try:
        initializeVectors(x, y, filePath)
        calculateLine(x, y, line)
        predicted = calculatePredicted(x, line)
        errors = calculateErrors(x, y, line, predicted, errors)
        writeToFile(x, y, line, predicted, errors)
        print(f'Output has been created in the directory')

    except Exception as er: 
        print(f'Error: {er}')
        try:
            print(f"Unable to make calculations, please input values manually.")
            inputManual(x, y)
            calculateLine(x, y, line)
            predicted = calculatePredicted(x, line)
            errors = calculateErrors(x, y, line, predicted, errors)
            writeToFile(x, y, line, predicted, errors)
            print(f'Output has been created in the directory')


        except Exception as e:
            print(traceback.format_exc())
            print(f"Error occured: {e}")
    
if __name__ == "__main__":
    main()

    