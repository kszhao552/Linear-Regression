from LinearRegression import LinearRegression

import PySimpleGUI as sg

layout = [[sg.Text('Select a file:')], [sg.FileBrowse()],
         [sg.Button("Next")]]

window = sg.Window("Linear Regression", layout)

while True:
    event, values = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()