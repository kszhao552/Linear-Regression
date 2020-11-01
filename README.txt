This is a simple script designed to make calculations for values related to linear regressions easier.

LinearRegression.py: The program is designed to take in two vectors as input and will print out values related to the regression, including xbar, ybar, bhat1, bhat2, SSxx, SSxy, etc. The output will be written into a .txt file in case the data needs to be used in the future. The x, y, predicted y, and error lists will be placed into a csv file to be read easily.
To use the script, place all the .py files into the same directory. The script will prompt you to input the file path for a csv file. If the file is not valid, then it will prompt you to input the values manually. After that, the output files will be placed in the same directory as the script.

UserInterface.py: This script will create a simple gui that will make selecting your input file much easier. It will calculate the same values as LinearRegression.py and output the same files as it.
After running it, select the file. If there are any errors, it will bring a pop up and not continue on. Afterwards, it will display a graph of the regression with the points ploted.
BEWARE: The graph will not show axis if the value 0 is not in the range of values, so the graph will not display a scale and will be not reliable.