# Code to plot the Fisher's data set data to compare species wrt sepal and petal dimensional ratios
# Barry Clarke
# Rev2 - 19th Apr 2019 - Update to customise colour coding of data to be same as comparison.py
#                      - Incorporate table of stats for ratios

import matplotlib.pyplot as plt
import matplotlib.cm as cm # Used for designating colors to particular plots
import pandas as pd
import numpy as np
import datetime
import csv

# Unlike comparison.py, using dataframes to manipluate data in this program
df = pd.read_csv('iris.csv', index_col=None)

# Input a global title
fig = plt.figure()                   # https://stackoverflow.com/questions/7526625/matplotlib-global-legend-and-title-aside-subplots
st = fig.suptitle("Comparison of dimension ratios for Sepal and Petal", fontsize="x-large", fontweight="bold")

# Plot the ratio of Sepal length to Sepal width
plt.subplot(1,2,1)
ratio1 = df["sepal_length"]/df["sepal_width"]
for name, group in df.groupby("species"):   # plot the data by specie. ref: https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
    # designating specific colours for each group of specie. Ref: https://towarddatascience.com/customizing-plots-with-python-matplotlib-bcf02691931f
    if name=='setosa':
        colors = ['#FF0000'] 
    elif name=='versicolor':
        colors = ['#0000ff']
    else:
        colors = ['#008000']
    plt.scatter(group.index, ratio1[group.index], label=name, color = colors)
    plt.title("Ratio of Sepal length vs Sepal width", fontweight='bold')
    plt.xlabel("Sample")
    plt.ylabel("Ratio")
    plt.axis([0,150, 0,3])


# Plot the ratio of Petal length vs Petal width
plt.subplot(1,2,2)
ratio2 = df["petal_length"]/df["petal_width"]
for name, group in df.groupby("species"):
    if name=='setosa':
        colors = ['#FF0000']
    elif name=='versicolor':
        colors = ['#0000ff']
    else:
        colors = ['#008000']
    plt.scatter(group.index, ratio2[group.index], color = colors)
    plt.title("Ratio of Petal length vs Petal width", fontweight='bold')
    plt.xlabel("Sample")
    plt.ylabel("Ratio")
    plt.axis([0,150, 0,16])

# adjusting the size of the subplots to allow for room for the legend at the top of the subplots.
fig.subplots_adjust(left=None, bottom=None, right=None, top=0.9)    #Ref: https://stackoverflow.com/questions/39164828/global-legend-for-all-subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3)

plt.show()

# Calculating the mean and standard deviation for the ratios of each specie
meansetsep = np.mean(ratio1[0:49]) # Avearge of the sepal length/sepal width for the Setosa
stdsetsep = np.std(ratio1[0:49])   # Standard deviation of the sepal length/sepalwidth for the Setosa
meansetpet = np.mean(ratio2[0:49]) # Avearge of the petal length/petal width for the Setosa
stdsetpet = np.std(ratio2[0:49])   # Standard deviation of the petal length/petal width for the Setosa

meanversep = np.mean(ratio1[50:99]) # Avearge of the sepal length/sepal width for the Versicolor
stdversep = np.std(ratio1[50:99])   # Standard deviation of the sepal length/sepalwidth for the Versicolor
meanverpet = np.mean(ratio2[50:99]) # Avearge of the petal length/petal width for the Versicolor
stdverpet = np.std(ratio2[50:99])   # Standard deviation of the petal length/petal width for the Versicolor

meanvirsep = np.mean(ratio1[100:149]) # Avearge of the sepal length/sepal width for the Virginica
stdvirsep = np.std(ratio1[100:149])   # Standard deviation of the sepal length/sepalwidth for the Virginica
meanvirpet = np.mean(ratio2[100:149]) # Avearge of the petal length/petal width for the Virginica
stdvirpet = np.std(ratio2[100:149])   # Standard deviation of the petal length/petal width for the Virginica

# Create a csv filenme from the current date and time
filename  = datetime.datetime.strftime(datetime.datetime.now(), "Ratio_statistics_%d-%m-%Y.csv")

with open(filename, "w", newline='') as f:
    # Enable CSV writing to the file
    writer = csv.writer(f)
    writer.writerow(["", "", "length/width dimensional ratios", "", ""])
    # Write a header now
    writer.writerow(["Sepal or Petal?", "Statistic", "Setosa", "Versicolor", "Virginica"])
    writer.writerow(["Sepal", "Average", format(meansetsep, '.3f'), format(meanversep, '.3f'), format(meanvirsep, '.3f')])
    writer.writerow(["Sepal", "Std Dev", format(stdsetsep, '.3f'), format(stdversep,'.3f'), format(stdvirsep, '.3f')])
    writer.writerow(["Petal", "Average", format(meansetpet, '.3f'), format(meanverpet, '.3f'), format(meanvirpet, '.3f')])
    writer.writerow(["Petal", "Std Dev", format(stdsetpet, '.3f'), format(stdverpet,'.3f'), format(stdvirpet, '.3f')])
    writer.writerow([])   






