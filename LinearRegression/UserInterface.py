import LinearRegression
from regression import Regression
from vector import Vector
import PySimpleGUI as sg
import sys

layout = [[sg.Text('Select a file:')], 
         [sg.FileBrowse(file_types=(("CSV files", "*.csv"),)), sg.Input()],
         [sg.Button("Next"), sg.Button("Exit")]]

window = sg.Window("Linear Regression", layout)

line = Regression(0)
x = Vector(0)
y = Vector(0)
errors = Vector(0)
predicted = Vector(0)

while True:
    event, values = window.read()

    #Want to create a new window, if event is next.
    #But if the input file is empty, then we want to not continue on
    if event == "Next":
       if (values[0] == ""):
            sg.popup("Please select a file.")
       else:
           #Attempt to create the linear regression data from the input file.
           filePath = values[0]
           try:
                LinearRegression.initializeVectors(x, y, filePath)
                LinearRegression.calculateLine(x, y, line)
                predicted = LinearRegression.calculatePredicted(x, line)
                errors = LinearRegression.calculateErrors(x, y, line, predicted, errors)
                LinearRegression.writeToFile(x, y, line, predicted, errors)
                sg.popup("Output has been created")
                break
           except ValueError:
                sg.popup("Non-numerical value in data")
           except ZeroDivisionError:
               sg.popup("Values all on same x value or y value.")

    #If the user wants to input values individually, then we must prompt the user to do so.
    if event == "Exit":
        break

    if event == sg.WIN_CLOSED:
        window.close()
        sys.exit(0)


window.close()