#CB 30/03/2019
#GMIT Data Analytics Programming & Scripting Module 2019
#Project - Fishers Iris Dataset

import numpy as np # linear algebra
#import pandas as pd # data processing, CSV file I/O
data = np.genfromtxt('iris.csv', delimiter = ',')
firstcol = data[:,0]
secondcol = data[:,1]
thirdcol = data[:,2]
fourthcol = data[:,3]
meanfirstcol = np.mean(data[:,0])
meansecondcol = np.mean(data [:,1])
meanthirdcol = np.mean(data [:,2])
meanfourthcol = np.mean(data [:,3])
print ("Average of first column is: ", meanfirstcol)
print ("Average of second column is: ", meansecondcol)
print ("Average of third column is: ", meanthirdcol)
print ("Average of fourth column is: ", meanfourthcol)