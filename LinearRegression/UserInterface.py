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
                window.close()
                sg.popup("Output has been created")
                break
           except ValueError:
                sg.popup("Non-numerical value in data")
           except ZeroDivisionError:
               sg.popup("Values all on same x value or y value.")

    #If the user wants to input values individually, then we must prompt the user to do so.
    if event == "Exit":
        window.close()
        sys.exit(0)

    if event == sg.WIN_CLOSED:
        window.close()
        sys.exit(0)


#if we are here, then a regression has been made and we should be able to graph it.

layout1 = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(x.min, y.min), graph_top_right=(x.max,y.max), background_color='white', key='graph')],]    

window1 = sg.Window('Linear Regression', layout1, grab_anywhere=True).Finalize()    
graph = window1['graph']         # type: sg.Graph

# Draw axis    
graph.DrawLine((x.min,0), (x.max,0))    
graph.DrawLine((0,y.min), (0,y.max))    

for z in range(int(x.min), int(x.max), 20):    
    graph.DrawLine((z,-3), (z,3))    


for w in range(int(y.min), int(y.max), 20):    
    graph.DrawLine((-3,w), (3,w))    

for i in range(x.size):
    graph.DrawCircle((x.data[i], y.data[i]), 1, line_color='blue', fill_color='blue')


# Draw Graph    
for z in range(int(x.min) ,int(x.max)):    
    w = line.bhat0 + line.bhat1*z  
    graph.DrawCircle((z,w), 1, line_color='red', fill_color='red')    

while True:
    event, values = window1.read()  

    if event == sg.WIN_CLOSED:
        window.close()
        sys.exit(0)