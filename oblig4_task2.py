# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 18:50:37 2021

@author: alexa
"""


import numpy as np
from statsmodels.graphics.gofplots import qqplot

data1 = np.genfromtxt("data/katters_vekt.csv", delimiter=(','), usecols=2);
data2 = np.genfromtxt("data/katters_vekt.csv", delimiter =(','), usecols=3);

qqplot(data1,line='s');
qqplot(data2,line='s');





