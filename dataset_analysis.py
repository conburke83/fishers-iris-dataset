#CB 30/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Project - Fishers Iris Dataset

import numpy as np #Importing the numpy module to allow usage of inbuilt pyton functions for scientific 
#analysis
import csv #Importing the csv module to allow usage of inbuilt pyton functions for .csv files
import pandas as pd # Data processing, CSV file I/O

# The next section of code extracts the header names and inserts them into a list, to be used
# later in the code. 
with open('iris.csv', 'r') as f:
    reader = csv.reader(f)
    i = next(reader)
    rest = [row for row in reader]
# Importing the .csv file as a delimited file, skipping the header row, and naming it 'data'. 'Data' can be 
# called later in the program for perofmring calculations and analysis on the dataset 
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
meanfirstcol = np.mean(data[:,0])
meansecondcol = np.mean(data [:,1])
meanthirdcol = np.mean(data [:,2])
meanfourthcol = np.mean(data [:,3])
# Printing the output of each mean, bringing in the associated header name and also calling the 'cm' variable
print ("The average",(i[0]), "is: ", meanfirstcol, cm)
print ("The average",(i[1]), "is: ", meansecondcol, cm)
print ("The average",(i[2]), "is: ", meanthirdcol, cm)
print ("The average",(i[3]), "is: ", meanfourthcol, cm)

# 05/04/2019
# Code written to calculate the mean of each of the first 4 columns. Next block of work - Need to
# elaborate on this to make the program skip over the header row in the .csv file (rather than just 
# deleting it), and then include the header name i the print output, so the user knows what each
# printed mean value relates to"
# 06/04/2019
# Code written to calculate and print the mean of each of the first 4 columns. Setup some of the program 
# variables to be used throught out the program, such as i, data, cm, firstcol, etc. Next block of work - Use
# some further numpy functionality to perform more analysis, such as standard deviation, max and min, etc.
# Then look at creating some graphical representations of the findings.
