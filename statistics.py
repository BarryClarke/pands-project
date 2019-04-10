# Code to calculate basic stats for each specie of Fisher's Iris data set
# Barry Clarke
# Rev0 - 9th Apr 2019

import numpy as np
import datetime
import csv

# Read data file into array
data = np.genfromtxt('Data/iris.csv', delimiter=',')

# Selecting data for Sepal lengths of each specie 
setseplen = data[0:50,0]                # Selecting the data for Setosa Sepal Length
verseplen = data[50:100,0]              # Selecting the data for Versicolor Sepal Length
virseplen = data[100:150,0]             # Selecting the data for Virginica Sepal Length

# Selecting data for Sepal widths of each specie
setsepwid = data[0:50,1]                # Selecting the data for Setosa Sepal Width
versepwid = data[50:100,1]              # Selecting the data for Versicolor Sepal Width
virsepwid = data[100:150,1]             # Selecting the data for Virginica Sepal Width

# Selecting data for Petal lengths of each specie
setpetlen = data[0:50,2]                # Selecting the data for Setosa Petal Length
verpetlen = data[50:100,2]              # Selecting the data for Versicolor Petal Length
virpetlen = data[100:150,2]             # Selecting the data for Virginica Petal Length

# Selecting data for Petal widths of each specie
setpetwid = data[0:50,3]                # Selecting the data for Setosa Petal Width
verpetwid = data[50:100,3]              # Selecting the data for Versicolor Petal Width
virpetwid = data[100:150,3]             # Selecting the data for Virginica Petal Width


# Main statistics for each specie
# The Iris Setosa
# Sepal length
minsetseplen = np.min(setseplen)      # Minimum Sepal length of a Setosa
maxsetseplen = np.max(setseplen)      # Maximum Sepal length of a Setosa
meansetseplen = np.mean(setseplen)    # Average Sepal length of a Setosa
stddevsetseplen = np.std(setseplen)     # Standard deviation of the length of a Sepal of a Setosa
scatsetseplen = np.max(setseplen) - np.min(setseplen) # The scatter of Sepal length in the Setosa (ie Max length - Min length)
# Sepal width
minsetsepwid = np.min(setsepwid)      # Minimum Sepal width of a Setosa
maxsetsepwid = np.max(setsepwid)      # Maximum Sepal width of a Setosa
meansetsepwid = np.mean(setsepwid)    # Average Sepal width of a Setosa
stddevsetsepwid = np.std(setsepwid)     # Standard deviation of the width of a Sepal of a Setosa
scatsetsepwid = np.max(setsepwid) - np.min(setsepwid) # The scatter of Sepal width in the Setosa (ie Max width - Min width)
# Petal length
minsetpetlen = np.min(setpetlen)      # Minimum Petal length of a Setosa
maxsetpetlen = np.max(setpetlen)      # Maximum Petal length of a Setosa
meansetpetlen = np.mean(setpetlen)    # Average Petal length of a Setosa
stddevsetpetlen = np.std(setpetlen)     # Standard deviation of the length of a Petal of a Setosa
scatsetpetlen = np.max(setpetlen) - np.min(setpetlen) # The scatter of Petal length in the Setosa (ie Max length - Min length)
# Petal width
minsetpetwid = np.min(setpetwid)      # Minimum Petal width of a Setosa
maxsetpetwid = np.max(setpetwid)      # Maximum Petal width of a Setosa
meansetpetwid = np.mean(setpetwid)    # Average Petal width of a Setosa
stddevsetpetwid = np.std(setpetwid)     # Standard deviation of the width of a Petal of a Setosa
scatsetpetwid = np.max(setpetwid) - np.min(setpetwid) # The scatter of Petal width in the Setosa (ie Max width - Min width)

# The Iris Versicolor
# Sepal length
minverseplen = np.min(verseplen)    # Average Sepal length of a Versicolor
maxverseplen = np.max(verseplen)    # Average Sepal length of a Versicolor
meanverseplen = np.mean(verseplen)  # Average Sepal length of a Versicolor
stddevverseplen = np.std(verseplen)     # Standard deviation of the length of a Sepal of a Versicolor
scatverseplen = np.max(verseplen) - np.min(verseplen) # The scatter of Sepal length in the Versicolor (ie Max length - Min length)
# Sepal width
minversepwid = np.min(versepwid)    # Average Sepal width of a Versicolor
maxversepwid = np.max(versepwid)    # Average Sepal width of a Versicolor
meanversepwid = np.mean(versepwid)  # Average Sepal width of a Versicolor
stddevversepwid = np.std(versepwid)     # Standard deviation of the width of a Sepal of a Versicolor
scatversepwid = np.max(versepwid) - np.min(versepwid) # The scatter of Sepal width in the Versicolor (ie Max width - Min width)
# Petal length
minverpetlen = np.min(verpetlen)      # Minimum Petal length of a Versicolor
maxverpetlen = np.max(verpetlen)      # Maximum Petal length of a Versicolor
meanverpetlen = np.mean(verpetlen)    # Average Petal length of a Versicolor
stddevverpetlen = np.std(verpetlen)     # Standard deviation of the length of a Petal of a Versicolor
scatverpetlen = np.max(verpetlen) - np.min(verpetlen) # The scatter of Petal length in the Versicolor (ie Max length - Min length)
# Petal width
minverpetwid = np.min(verpetwid)      # Minimum Petal width of a Versicolor
maxverpetwid = np.max(verpetwid)      # Maximum Petal width of a Versicolor
meanverpetwid = np.mean(verpetwid)    # Average Petal width of a Versicolor
stddevverpetwid = np.std(verpetwid)     # Standard deviation of the width of a Petal of a Versicolor
scatverpetwid = np.max(verpetwid) - np.min(verpetwid) # The scatter of Petal width in the Versicolor (ie Max width - Min width)

# The Iris Virginica
# Sepal length
minvirseplen = np.min(virseplen)  # Average Sepal length of a Virginica
maxvirseplen = np.max(virseplen)  # Average Sepal length of a Virginica
meanvirseplen = np.mean(virseplen)  # Average Sepal length of a Virginica
stddevvirseplen = np.std(virseplen)     # Standard deviation of the length of a Sepal of a Virginica
scatvirseplen = np.max(virseplen) - np.min(virseplen) # The scatter of Sepal length in the Virginica (ie Max length - Min length)
# Sepal width
minvirsepwid = np.min(virsepwid)  # Average Sepal width of a Virginica
maxvirsepwid = np.max(virsepwid)  # Average Sepal width of a Virginica
meanvirsepwid = np.mean(virsepwid)  # Average Sepal width of a Virginica
stddevvirsepwid = np.std(virsepwid)     # Standard deviation of the width of a Sepal of a Virginica
scatvirsepwid = np.max(virsepwid) - np.min(virsepwid) # The scatter of Sepal width in the Virginica (ie Max width - Min width)
# Petal length
minvirpetlen = np.min(virpetlen)      # Minimum Petal length of a Virginica
maxvirpetlen = np.max(virpetlen)      # Maximum Petal length of a Virginica
meanvirpetlen = np.mean(virpetlen)    # Average Petal length of a Virginica
stddevvirpetlen = np.std(virpetlen)     # Standard deviation of the length of a Petal of a Virginica
scatvirpetlen = np.max(virpetlen) - np.min(virpetlen) # The scatter of Petal length in the Virginica (ie Max length - Min length)
# Petal width
minvirpetwid = np.min(virpetwid)      # Minimum Petal width of a Virginica
maxvirpetwid = np.max(virpetwid)      # Maximum Petal width of a Virginica
meanvirpetwid = np.mean(virpetwid)    # Average Petal width of a Virginica
stddevvirpetwid = np.std(virpetwid)     # Standard deviation of the width of a Petal of a Virginica
scatvirpetwid = np.max(virpetwid) - np.min(virpetwid) # The scatter of Petal width in the Virginica (ie Max width - Min width)

# Create a csv filenme from the current date and time
filename  = datetime.datetime.strftime(datetime.datetime.now(), "statistics_%d-%m-%Y.csv")

# Open the file with that filename
with open(filename, "w", newline='') as f:
    # Enable CSV writing to the file
    writer = csv.writer(f)
    writer.writerow(["", "", "Setosa", "", "", ""])
    # Write a header now
    writer.writerow(["Statistic", "Sepal length", "Sepal width", "Petal length", "Petal width", "Specie"])
    writer.writerow(["Minimum", minsetseplen, minsetsepwid, minsetpetlen, minsetpetwid, "Setosa"])
    writer.writerow(["Maximum", maxsetseplen, maxsetsepwid, maxsetpetlen, maxsetpetwid, "Setosa"])
    writer.writerow(["Scatter", format(scatsetseplen, '.3f'), format(scatsetsepwid, '.3f'), format(scatsetpetlen, '.3f'), format(scatsetpetwid, '.3f'), "Setosa"])
    writer.writerow(["Average", format(meansetseplen, '.3f'), format(meansetsepwid, '.3f'), format(meansetpetlen, '.3f'), format(meansetpetwid, '.3f'), "Setosa"])
    writer.writerow(["Std Dev", format(stddevsetseplen, '.3f'), format(stddevsetsepwid, '.3f'), format(stddevsetpetlen, '.3f'), format(stddevsetpetwid, '.3f'), "Setosa"])
    writer.writerow([])
    writer.writerow(["", "", "Versicolor", "", "", ""])
    writer.writerow(["Statistic", "Sepal length", "Sepal width", "Petal length", "Petal width", "Specie"])
    writer.writerow(["Minimum", minverseplen, minversepwid, minverpetlen, minverpetwid, "Versicolor"])
    writer.writerow(["Maximum", maxverseplen, maxversepwid, maxverpetlen, maxverpetwid, "Versicolor"])
    writer.writerow(["Scatter", format(scatverseplen, '.3f'), format(scatversepwid, '.3f'), format(scatverpetlen, '.3f'), format(scatverpetwid, '.3f'), "Versicolor"])
    writer.writerow(["Average", format(meanverseplen, '.3f'), format(meanversepwid, '.3f'), format(meanverpetlen, '.3f'), format(meanverpetwid, '.3f'), "Versicolor"])
    writer.writerow(["Std Dev", format(stddevverseplen, '.3f'), format(stddevversepwid, '.3f'), format(stddevverpetlen, '.3f'), format(stddevverpetwid, '.3f'), "Versicolor"])
    writer.writerow([])
    writer.writerow(["", "", "Virginica", "", "", ""])
    writer.writerow(["Statistic", "Sepal length", "Sepal width", "Petal length", "Petal width", "Specie"])
    writer.writerow(["Minimum", minvirseplen, minvirsepwid, minvirpetlen, minvirpetwid, "Virgninica"])
    writer.writerow(["Maximum", maxvirseplen, maxvirsepwid, maxvirpetlen, maxvirpetwid, "Virgninica"])
    writer.writerow(["Scatter", format(scatvirseplen, '.3f'), format(scatvirsepwid, '.3f'), format(scatvirpetlen, '.3f'), format(scatvirpetwid, '.3f'), "Virgninica"])
    writer.writerow(["Average", format(meanvirseplen, '.3f'), format(meanvirsepwid, '.3f'), format(meanvirpetlen, '.3f'), format(meanvirpetwid, '.3f'), "Virgninica"])
    writer.writerow(["Std Dev", format(stddevvirseplen, '.3f'), format(stddevvirsepwid, '.3f'), format(stddevvirpetlen, '.3f'), format(stddevvirpetwid, '.3f'), "Virgninica"])
    