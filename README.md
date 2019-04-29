# fishers-iris-dataset
Repository for the fishers-iris-dataset project (GMIT 2019 Data-Analytics Programming and Scripting module)
Conor Burke 30th March 2019

References:
file:///C:/Users/conor/AppData/Local/Packages/Microsoft.MicrosoftEdge_8wekyb3d8bbwe/TempState/Downloads/project.pdf
https://web.microsoftstream.com/video/2d4fec98-175e-4a12-a07e-bd096f40fc3c
http://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
https://www.kaggle.com/bmaria/iris-dataset
http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame
https://www.numpy.org/
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://gist.github.com/curran/a08a1080b88344b0c8a7
https://stackoverflow.com/questions/28836781/reading-column-names-alone-in-a-csv-file/35963291
https://cmdlinetips.com/2018/01/how-to-get-unique-values-from-a-column-in-pandas-data-frame/
https://stackoverflow.com/questions/5982206/how-to-print-a-linebreak-in-a-python-function
https://www.geeksforgeeks.org/round-function-python/
https://stackoverflow.com/questions/34050491/standard-deviation-in-numpy
https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python
https://matplotlib.org/users/pyplot_tutorial.html
https://stackoverflow.com/questions/26597116/seaborn-plots-not-showing-up
https://stackoverflow.com/questions/30336324/seaborn-load-dataset
https://github.com/f90/Wave-U-Net/issues/11
https://stackoverflow.com/questions/37815774/seaborn-pairplot-legend-how-to-control-position?noredirect=1&lq=1
https://seaborn.pydata.org/tutorial/axis_grids.html

Summary Description of the Dataset
Fisher's Iris dataset is a multivariate dataset created by British statistician and biologist Ronald Fisher (with the assistance of Edgar Anderson) in a 1936 scientific paper examining the use of multiple measurements in taxonomic problems. The dataset represents a good example of linear discriminant analysis. Linear discriminant analysis is a method used in statistics to find a linear combination of features that characterizes or separates two or more classes of objects or events.
The data-set consists of 50 samples from three species (150 samples in total) of the Iris flower (Iris setosa, Iris virginica and Iris versicolor). The samples were "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus". 
Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
The dataset therefore contains 5 columns in total.
 - SepalLengthCm
 - SepalWidthCm
 - PetalLengthCm
 - PetalWidthCm
 - Species
(Note, some modified instances of the dataset found online contain a sixth column 'ID', being a unique identifier for each sample).
One of the most interesting things about the datset as shown by analysis is that one species is linearly separable from the other two, but the other two are not linearly comparable to each other.  Fisher's linear discriminant model can only be obtained when the object species are known
Due to these characteristics of the dataset it has become famous for use as a test-case and in the teaching of statistics, pattern recognition, machine learning, data-mining and data analysis.

Summary of the Analysis Performed
Calculated and analysed the Average, Maximum, Minimum, Range and Standard Deviation for each of Sepal Length, Sepal Width, Petal Length and Petal Width.
Created graphical representations of the data. Specifically, histograms and scatter diagrams for each combination of Sepal Length, Sepal Width, Petal Length, Petal Width versus Sepal Length, Sepal Width, Petal Length, Petal Width. 16 plots created in total, covering all of these different x-axis versus y-axis combinations.

Summary of the Results
The main observation from the analysis is that there is linear discrimination of the species Setosa. This is particularly noticable in the plots showing the visual representations of the data. Species Versicolour and Virginica are linearly aligned to on another, while Setosa is linearly seperated from them.