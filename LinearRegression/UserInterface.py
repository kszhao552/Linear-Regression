from LinearRegression import LinearRegression

import PySimpleGUI as sg

layout = [[sg.Text('Select a file:')], 
         [sg.FileBrowse(file_types=(("CSV files", "*.csv"),)), sg.Input()],
         [sg.Button("Next"), sg.Button("Input Values Manually")]]

window = sg.Window("Linear Regression", layout)

while True:
    event, values = window.read()
    if event == "Next" or event == sg.WIN_CLOSED:
        break

window.close()