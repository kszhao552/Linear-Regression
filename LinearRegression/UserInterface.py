from LinearRegression import LinearRegression

import PySimpleGUI as sg

layout = [[sg.Text('Select a file:')], 
         [sg.FileBrowse(file_types=(("CSV files", "*.csv"),)), sg.Input()],
         [sg.Button("Next"), sg.Button("Input Values Manually")]]

window = sg.Window("Linear Regression", layout)

while True:
    event, values = window.read()

    #Want to create a new window, if event is next.
    #But if the input file is empty, then we want to not continue on
    if event == "Next":
       if (values[0] == ""):
           sg.popup("Please select a file.")
       else:
            break

    #If the user wants to input values individually, then we must prompt the user to do so.
    if event == "Input Values Manually":
        break

    if event == sg.WIN_CLOSED:
        break

window.close()