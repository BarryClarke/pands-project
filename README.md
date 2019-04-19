# Fisher's Iris Data set
![The Iris Family](/Images/iris-machinelearning.png)
## Scope
To summarize and present analysis of Fisher's Iris data set. Programming and Scripting Module project 2019
[See here for instructions](https://github.com/ianmcloughlin/project-pands/raw/master/project.pdf)
## Table of Contents
1. Background
    - Ronald Fisher
    - Fisher's Iris data set
2. Data set Introduction
3. Analysing the data set
    - 3.1 Analysis of each individual specie
    - 3.2 Comparison of species for each individual attribute
4. Final Thoughts
5. References

## 1. Background
### Ronald Fisher 
![Ronald Fisher](/Images/Ronald.Fisher.jpg)  
[Ronald Fisher](http://leansixsigmadefinition.com/glossary/ronald-fisher/)  
* British Biologist and statistician (17th February 1890 - 29th July 1962)
* Widely considered to be "the single most important figure in 20th century statistics" *[2]*
* First to propose the Design of Experiments (The Design of Experiments (1935))
* Credited with initiating methods which led to Six Sigma and Lean Manufacturing [Lean Manufacturing and Six Sigma](http://leansixsigmadefinition.com/glossary/six-sigma/)
* Responsible for many other statistcal techniques such as [Analysis of Variance](http://leansixsigmadefinition.com/glossary/anova/), [P-value](https://en.wikipedia.org/wiki/P-value), and [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)

### Fisher's Iris dataset
* Linear Discriminant Analysis (LDA) is a statistiacl technique used in many applications including machine learning, image recognition and genetics. It focuses on maximising the seperability between two groups among known categories in order to differentiate the two groups and hence allow decisions to be made regarding the categories. 
* A good example of the application of LDA would be deciding which patients, with a particular illness, should be treated with a specific drug and which should not. LDA is a statistical technique that can use genetics to determine this with high statistical accuracy. See the following video: [Statquest: Linear Discriminant Analysis](https://www.youtube.com/watch?v=azXCzI57Yfc). *[5]*
* Fisher's Iris data set is a multivariate data set introduced by Ronald Fisher in his 1936 paper *[The use of multiple measurements in taxonomic problems](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x)* *[3]* as an example of Linear discriminant analysis.

## 2. Data set Introduction
* The Iris data set contains a total of 150 records - 50 records per specie, for 3 species of Iris: Iris Setosa, Iris Versicolor, and Iris Virginica. Within each record there are 5 attributes: the Sepal length, the Sepal width, the Petal length, the Petal width, and the specie.*[1]* The raw data colected can be seen [here](iris.csv). *[6]*
* Two of the three species (Setosa and Versicolor) were collected in Gaspé Peninsula, all from the same pasture, picked on the same day and measured at the same time by the same person with the same apparatus.*[4]*
* This data set and subsequent analysis has proven very valuable in many area's, including machine learning, because of the interesting statistical properties containied within the data set: From the data, one of the species is easy to seperate from the other two, but the other two similar species are difficult to seperate.

## 3. Analysing the data set
### 3.1 Analysis of each individual specie
As can be seen in the header picture, each Iris specie has a Sepal and a Petal. From the measurements of the lengths and widths of both the Sepal and the Petal, we have calculated a few basic statistics for each specie. Please see the results below for the minimum, maximum, and average lengths and widths of sepal and petal for each specie, along with the scatter (Max - min) and the standard deviation for each attribute.
![statistics.png](/Images/statistics.png) 
These stats were calculated and presented in the above table using [statistics.py](statistics.py). By running this program [statistics_10-04-2019.csv](statistics_10-04-2019.csv) is generated.

### 3.2 Comparison of species for individual attributes
In order to compare and contrast each specie, please see the below plots ![Comparison_of_Iris_species_for_individual_attributes.png](/Images/Comparison_of_Iris_species_for_individual_attributes.png) These plots were produced by running [comparison.py](comparison.py) and the resulting plots saved to [Comparison_of_Iris_species_for_individual_attributes.png](/Images/Comparison_of_Iris_species_for_individual_attributes.png) in the Images folder of the directory. 
From these plots, we can make a number of observations:
1. The sepal lengths and sepal widths for all 3 species are pretty similar, whereas there appears to be a difference in the petal length and petal widths across the 3 species.
2. The Setosa petal length and width clearly varies from the Versicolor and Virginica petal lengths and widths. It has a smaller petal. It is is quite easy to differentiate the Setosa from the other two species on the basis of the petal dimensions
3. It is more difficult to differentiate the Versicolor and the Virginica. As the plots show, although the Versicolor petal is slightly smaller in both length and width than the Virginica, there is still some crossover in the data for the Versicolor and Virginica petal. This means that, given a random petal, it would be difficult to decide whether it was a Versicolor or a Virginica.
4. The above gives us a good idea of the motivation of Fisher in his 1936 paper relating to the iris data set: Given a set of data from different entities, use Linear Discriminant Analysis seperate or differentiate one from another. The ability to apply statistics and mathematics to such a problem was groundbreaking and is why Fisher's paper and this data set is referenced and applied in so many area's to this day

### 3.3 Fisher's work on the data set



## 4. Final Thoughts

## 5. References
*1.* http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394/WholeStory-Iris.html  
*2.* http://leansixsigmadefinition.com/glossary/ronald-fisher/  
*3.* R.A. Fisher (1936). ["The use of multiple measurements in taxonomic problems"](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x). Annals of Eugenics. **7**(2): 179-188  
*4.* https://en.wikipedia.org/wiki/Iris_flower_data_set  
*5.* https://www.youtube.com/watch?v=azXCzI57Yfc  
*6.* https://gist.github.com/curran/a08a1080b88344b0c8a7

comparison.py: https://matplotlib.org/gallery/subplots_axes_and_figures/subplot.html







