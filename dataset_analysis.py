#CB 30/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Project - Fishers Iris Dataset

import numpy as np #Importing the numpy module to allow usage of inbuilt pyton functions for scientific analysis
import csv #Importing the csv module to allow usage of inbuilt pyton functions for .csv files
import pandas as pd # Data processing, CSV file I/O

# The next section of code extracts the header names and inserts them into a list, to be used
# later in the code. Reference 
with open('iris.csv', 'r') as f:
    reader = csv.reader(f)
    i = next(reader)
    rest = [row for row in reader]
data = np.genfromtxt('iris.csv', delimiter = ',')[1:]
#lines = data.readlines()[1:]
cm = str("cm")
firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]
meanfirstcol = np.mean(data[:,0])
meansecondcol = np.mean(data [:,1])
meanthirdcol = np.mean(data [:,2])
meanfourthcol = np.mean(data [:,3])
print ("The average",(i[0]), "is: ", meanfirstcol, cm)
print ("The average",(i[1]), "is: ", meansecondcol, cm)
print ("The average",(i[2]), "is: ", meanthirdcol, cm)
print ("The average",(i[3]), "is: ", meanfourthcol, cm)

#Code written to calculate the mean of each of the first 4 columns. Next block of work - Need to
# elaborate on this to make the program skip over the header row in the .csv file (rather than just 
# deleting it), and then include the header name i the print output, so the user knows what each
#  printed mean value relates to"