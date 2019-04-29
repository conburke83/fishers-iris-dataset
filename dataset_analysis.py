# CB 30/03/2019
# GMIT Data Analytics Programming & Scripting Module 2019
# Project - Fishers Iris Dataset

import numpy as np # Importing the numpy module to allow usage of inbuilt pyton functions for scientific 
# analysis
import csv # Importing the csv module to allow usage of inbuilt pyton functions for .csv files
import pandas as pd # Data processing, CSV file I/O
import matplotlib.pyplot as plt #Importing the pyplot function of the matplotlib module, for creating graphs
import seaborn as sns #Importing the seaborn module, for creating graphs

# Using pandas to import the iris.csv file and creating a dataframe named 'fishers_iris_csv'
fishers_iris_csv = 'iris.csv'
fishers_iris = pd.read_csv(fishers_iris_csv)
# Printing the data frame basic info, for the benefit of the user
print (fishers_iris.info())
# Creating a list of the unique values of species, and naming the list 'species_list'
species_list = fishers_iris['species'].unique().tolist()
# Printing 'Species List'
print (species_list)
# Print a line break
print ('\n')

# The next section of code extracts the header names and inserts them into a list, to be used
# later in the code. 
with open('iris.csv', 'r') as f:
    reader = csv.reader(f)
    i = next(reader)
    rest = [row for row in reader]
# Importing the .csv file as a delimited file, skipping the header row, and naming it 'data'. 'Data' can be 
# called later in the program for performing calculations and analysis on the dataset 
data = np.genfromtxt('iris.csv', delimiter = ',')[1:]
# Creating a simple variable 'cm' to store the string "cm" for use in strings later in the program
cm = str("cm")
# Creating four variables to store the data from columns 1 to 4 individually, for use in calculations later 
# in the program
firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]
# Creating four variables to calculate and store the mean of each column, using the numpy funtion 'mean'.
meanfirstcol = round(np.mean(data[:,0]),2)
meansecondcol = round(np.mean(data [:,1]),2)
meanthirdcol = round(np.mean(data [:,2]),2)
meanfourthcol = round(np.mean(data [:,3]),2)
# Printing the output of each mean, bringing in the associated header name and also calling the 'cm' variable
print ("The average",(i[0]), "is", meanfirstcol, cm)
print ("The average",(i[1]), "is", meansecondcol, cm)
print ("The average",(i[2]), "is", meanthirdcol, cm)
print ("The average",(i[3]), "is", meanfourthcol, cm)
# Print a line break
print ('\n')

# Creating four variables to calculate and store the maximum value of each column, using the numpy funtion 'max'.
maxfirstcol = round(np.max(data[:,0]),2)
maxsecondcol = round(np.max(data [:,1]),2)
maxthirdcol = round(np.max(data [:,2]),2)
maxfourthcol = round(np.max(data [:,3]),2)
# Printing the output of each maximum, bringing in the associated header name and also calling the 'cm' variable
print ("The maximum",(i[0]), "is", maxfirstcol, cm)
print ("The maximum",(i[1]), "is", maxsecondcol, cm)
print ("The maximum",(i[2]), "is", maxthirdcol, cm)
print ("The maximum",(i[3]), "is", maxfourthcol, cm)
# Print a line break
print ('\n')

# Creating four variables to calculate and store the minimum value of each column, using the numpy funtion 'min'.
minfirstcol = round(np.min(data[:,0]),2)
minsecondcol = round(np.min(data [:,1]),2)
minthirdcol = round(np.min(data [:,2]),2)
minfourthcol = round(np.min(data [:,3]),2)
# Printing the output of each minimum, bringing in the associated header name and also calling the 'cm' variable
print ("The minimum",(i[0]), "is", minfirstcol, cm)
print ("The minimum",(i[1]), "is", minsecondcol, cm)
print ("The minimum",(i[2]), "is", minthirdcol, cm)
print ("The minimum",(i[3]), "is", minfourthcol, cm)
# Print a line break
print ('\n')

# Creating four variables to calculate and store the range of each column.
firstcolrange = round((maxfirstcol-minfirstcol),2)
secondcolrange = round((maxsecondcol-minsecondcol),2)
thirdcolrange = round((maxthirdcol-minthirdcol),2)
fourthcolrange = round((maxfourthcol-minfourthcol),2)
# Printing the output of each range, bringing in the associated header name and also calling the 'cm' variable
print ("The range for",(i[0]), "is", firstcolrange, cm)
print ("The range for",(i[1]), "is", secondcolrange, cm)
print ("The range for",(i[2]), "is", thirdcolrange, cm)
print ("The range for",(i[3]), "is", fourthcolrange, cm)
# Print a line break
print ('\n')

# Creating four variables to calculate and store the range of each column.
stdevfirstcol = round(np.std(data[:,0]),2)
stdevsecondcol = round(np.std(data [:,1]),2)
stdevthirdcol = round(np.std(data [:,2]),2)
stdevfourthcol = round(np.std(data [:,3]),2)
# Printing the output of each range, bringing in the associated header name and also calling the 'cm' variable
print ("The standard deviation for",(i[0]), "is", stdevfirstcol, cm)
print ("The standard deviation for",(i[1]), "is", stdevsecondcol, cm)
print ("The standard deviation for",(i[2]), "is", stdevthirdcol, cm)
print ("The standard deviation for",(i[3]), "is", stdevfourthcol, cm)
# Print a line break
print ('\n')

# Importing the 'Iris' dataset from the Seaborn online dataset repository on Github, and giving it the
# variable name 'iris'
iris = sns.load_dataset("iris")
# Creating variable 'g' and calling the Seaborn function pairplot into the variable. The pairplot function
# contains a palette of pre-defined plots which will be mapped for the given dataset. Within this variable we 
# are also defining the aesthetics to be used for the plots. 'Hue' and 'palette' define the colour system for
# the plots. 'Markers' defines the type of symbol used to mark the data-points in the plot. 'Height' defines
# the height of each plot in inches. 'Plot_kws' defines further attributes for the data-points in the plot.
g = sns.pairplot(iris,hue='species', palette='husl', markers='+', height=2.5, plot_kws=
    {"s":30,"alpha":1,'lw':1,'edgecolor':'w'})
# Save the plots as a .png image file in present working directory.
g.savefig('Test.png')
# Display the plots on screen for the user.
plt.show()


# 05/04/2019
# Code written to calculate the mean of each of the first 4 columns. Next block of work - Need to
# elaborate on this to make the program skip over the header row in the .csv file (rather than just 
# deleting it), and then include the header name in the print output, so the user knows what each
# printed mean value relates to.
# 06/04/2019
# Code written to calculate and print the mean of each of the first 4 columns. Setup some of the program 
# variables to be used throught out the program, such as i, data, cm, firstcol, etc. Next block of work - Use
# some further numpy functionality to perform more analysis, such as standard deviation, max and min, etc.
# Then look at creating some graphical representations of the findings.
# 09/04/2019
# Code written to calculate and print the max, min, range and standard deviation. Code added to round the
# output values to 2 decimal places. Added code to convert the dataset to a Pandas dataframe, and print the
# basic dataframe info. Next blocks of work - Aggregate some of the calculated data by species. creating some
# graphical representations of the findings. Export the output to a text file.

