# Code to plot the Fisher's data set data for  individual attributes and compare species
# Barry Clarke
# Rev0 - 19th Apr 2019

import matplotlib.pyplot as plt
import pandas as pd

# Unlike comparison.py, using dataframes to manipluate data in this program
df = pd.read_csv('iris.csv', index_col=None)

# Input a global title
fig = plt.figure()                   # https://stackoverflow.com/questions/7526625/matplotlib-global-legend-and-title-aside-subplots
st = fig.suptitle("Comparison of dimension ratios for Sepal and Petal", fontsize="x-large", fontweight="bold")

# Plot the ratio of Sepal length to Sepal width
plt.subplot(1,2,1)
ratio1 = df["sepal_length"]/df["sepal_width"]
for name, group in df.groupby("species"):   # plot the data by specie. ref: https://stackoverflow.com/questions/45862223/use-different-colors-in-scatterplot-for-iris-dataset
    plt.scatter(group.index, ratio1[group.index], label=name)
    plt.title("Ratio of Sepal length vs Sepal width", fontweight='bold')
    plt.xlabel("Sample")
    plt.ylabel("Ratio")
    plt.axis([0,150, 0,3])

# Plot the ratio of Petal length vs Petal width
plt.subplot(1,2,2)
ratio2 = df["petal_length"]/df["petal_width"]
for name, group in df.groupby("species"):
    plt.scatter(group.index, ratio2[group.index])
    plt.title("Ratio of Petal length vs Petal width", fontweight='bold')
    plt.xlabel("Sample")
    plt.ylabel("Ratio")
    plt.axis([0,150, 0,16])

# adjusting the size of the subplots to allow for room for the legend at the top of the subplots.
fig.subplots_adjust(left=None, bottom=None, right=None, top=0.9)    #Ref: https://stackoverflow.com/questions/39164828/global-legend-for-all-subplots
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=3)

plt.show()