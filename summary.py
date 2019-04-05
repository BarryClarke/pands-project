# Code to summarise Fisher's Iris data set
# Barry Clarke
# Rev0 - 5th Apr 2019

import numpy as np 

# Read data file into array
data = np.genfromtxt('Data/iris.csv', delimiter=',')

# Analysing the data for sepal length
setseplen = data[0:50,0]                # setseplen = Selecting the data for Setosa Sepal Length
verseplen = data[50:100,0]              # verseplen = Selecting the data for Versicolor Sepal Length
virseplen = data[100:150,0]             # virseplen = Selecting the data for Virginica Sepal Length

minsetseplen = np.min(data[0:50,0])      # Minimum Sepal length of a Setosa
maxsetseplen = np.max(data[0:50,0])      # Maximum Sepal length of a Setosa
meansetseplen = np.mean(data[0:50,0])    # Average Sepal length of a Setosa
scatsetseplen = np.max(data[0:50,0]) - np.min(data[0:50,0]) # The scatter of sepal length in the Setosa (ie Max length - Min length)

minverseplen = np.min(data[50:100,0])    # Average Sepal length of a Versicolor
maxverseplen = np.max(data[50:100,0])    # Average Sepal length of a Versicolor
meanverseplen = np.mean(data[50:100,0])  # Average Sepal length of a Versicolor
scatverseplen = np.max(data[50:100,0]) - np.min(data[50:100,0]) # The scatter of sepal length in the Versicolor

minvirseplen = np.min(data[100:150,0])  # Average Sepal length of a Virginica
maxvirseplen = np.max(data[100:150,0])  # Average Sepal length of a Virginica
meanvirseplen = np.mean(data[100:150,0])  # Average Sepal length of a Virginica
scatvirseplen = np.max(data[100:150,0]) - np.min(data[100:150,0]) # The scatter of sepal length in the Virginica

print("The data collected for Setosa sepal length is: \n", setseplen)
print("The minumum sepal length of a Setosa is: ", minsetseplen)
print("The maximum sepal length of a Setosa is: ", maxsetseplen)
print("The average sepal length of a Setosa is: ", format(meansetseplen, '.1f')) #ref https://docs.python.org/3/tutorial/floatingpoint.html for printing a number with limited decimal places 
print("The scatter of sepal length in the setosa is: ", format(scatsetseplen, '.1f'))
print()
print("The data collected for Versicolor sepal length is: \n", verseplen)
print("The minimum sepal length of a Versicolor is: ", minverseplen)
print("The maximum sepal length of a Versicolor is: ", maxverseplen)
print("The average sepal length of a Versicolor is: ", format(meanverseplen, '.1f'))
print("The scatter of sepal length in the Versicolor is: ", format(scatverseplen, '.1f'))
print()
print("The data collected for Virginica sepal length is: \n", virseplen)
print("The minimum sepal length of a Virginica is: ", minvirseplen)
print("The maximum sepal length of a Virginica is: ", maxvirseplen)
print("The average sepal length of a Virginica is: ", format(meanvirseplen, '.1f'))
print("The scatter of sepal length in the Virginica is: ", format(scatvirseplen, '.1f'))
