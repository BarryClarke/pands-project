# Code to summarise Fisher's Iris data set
# Barry Clarke
# Rev1 - 6th Apr 2019

import numpy as np
import pandas as pd 
import matplotlib.pyplot as pyplot 
import pylab 

# Read data file into array
data = np.genfromtxt('Data/iris.csv', delimiter=',')

# Reviewing each attribute of each specie
# Inputting a global title
fig = pyplot.figure()                   # https://stackoverflow.com/questions/7526625/matplotlib-global-legend-and-title-aside-subplots
st = fig.suptitle("Comparison of Iris species for individual attributes", fontsize="x-large", fontweight="bold")

# Analysing the data for sepal length
setseplen = data[0:50,0]                # setseplen = Selecting the data for Setosa Sepal Length
verseplen = data[50:100,0]              # verseplen = Selecting the data for Versicolor Sepal Length
virseplen = data[100:150,0]             # virseplen = Selecting the data for Virginica Sepal Length

# Plot the sepal length data for all 3 species on the same graph
pyplot.subplot(2,2,1)                   # Ref https://matplotlib.org/gallery/subplots_axes_and_figures/subplot.html for plotting many plots
pyplot.plot(setseplen, 'ro', verseplen, 'bo', virseplen, 'go') # Ref https://matplotlib.org/users/pyplot_tutorial.html
pyplot.title('Sepal Length', fontweight='bold')
pyplot.ylabel('Centimeter')
pyplot.axis([0,50, 0, 8])

# Analysing the data for sepal width
setsepwid = data[0:50,1]                # setseplen = Selecting the data for Setosa Sepal Width
versepwid = data[50:100,1]              # verseplen = Selecting the data for Versicolor Sepal Width
virsepwid = data[100:150,1]             # virseplen = Selecting the data for Virginica Sepal Width

# Plot the sepal width data for all 3 species on the same graph
pyplot.subplot(2,2,3)
pyplot.plot(setsepwid, 'ro', versepwid, 'bo', virsepwid, 'go')
pyplot.title('Sepal Width', fontweight='bold')
pyplot.xlabel('sample number')
pyplot.ylabel('Centimeter')
pyplot.axis([0,50, 0, 5])

# Analysing the data for petal length
setpetlen = data[0:50,2]                # setseplen = Selecting the data for Setosa Petal Length
verpetlen = data[50:100,2]              # verseplen = Selecting the data for Versicolor Petal Length
virpetlen = data[100:150,2]             # virseplen = Selecting the data for Virginica Petal Length

# Plot the petal length data for all 3 species on the same graph
pyplot.subplot(2,2,2)
pyplot.plot(setpetlen, 'ro', verpetlen, 'bo', virpetlen, 'go')
pyplot.title('Petal Length', fontweight='bold')
pyplot.ylabel('Centimeter')
pyplot.axis([0,50, 0, 8])

# Analysing the data for petal width
setpetwid = data[0:50,3]                # setseplen = Selecting the data for Setosa Petal Width
verpetwid = data[50:100,3]              # verseplen = Selecting the data for Versicolor Petal Width
virpetwid = data[100:150,3]             # virseplen = Selecting the data for Virginica Petal Width

# Plot the petal width data for all 3 species on the same graph
pyplot.subplot(2,2,4)
pyplot.plot(setpetwid, 'ro', verpetwid, 'bo', virpetwid, 'go')
pyplot.title('Petal Width', fontweight='bold')
pyplot.xlabel('sample number')
pyplot.ylabel('Centimeter')
pyplot.axis([0,50, 0, 5])

#pyplot.legend((setseplen, verseplen, virseplen), ('Setosa', 'Versicolor', 'Virginica')) 
#pylab.legend(loc='upper center')
pyplot.show()
#---------------------------------------------------------------------------------------------------------------------------------------------

# Main statistics for each specie
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
