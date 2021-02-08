# -*- coding: utf-8 -*-

import numpy as np

data = np.genfromtxt('data.csv', delimiter=',') 
#print(data)

#Mean
mean = np.round(np.mean(data), 2)
print("Gjennomsnitt " , mean)


#Median
median = np.round(np.median(data), 2)
print("Median" , median)

#Variance
variance = np.round(np.var(data, ddof =1),2)
print("Varians" , variance)


#Standard deviation
std = np.round(np.std(data,ddof=1),2)
print("Standardavvik" , std)

