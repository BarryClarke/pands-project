# Code to plot the Fisher's data set data for  individual attributes and compare species
# Barry Clarke
# Rev2 - 10th Apr 2019

import numpy as np 
import matplotlib.pyplot as pyplot  

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
pyplot.plot(setseplen, 'ro', label='Setosa') 
pyplot.plot(verseplen, 'bo', label='Versicolor') 
pyplot.plot(virseplen, 'go', label='Virginica') 
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
pyplot.axis([0,50, 0, 8])

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
pyplot.axis([0,50, 0, 8])

# adjusting the size of the subplots to allow for room for the legend at the top of the subplots. 
fig.subplots_adjust(left=None, bottom=None, right=None, top=0.9)    #Ref: https://stackoverflow.com/questions/39164828/global-legend-for-all-subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3)

pyplot.show()

