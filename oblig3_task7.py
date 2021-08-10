# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:01:55 2021

@author: alexa
"""

import numpy as np
from scipy.stats import poisson 
import matplotlib.pyplot as plt


parameter = float(input("Input parameter: "));
limit = float(input("Input - limit: "));

x = np.arange(0,limit+1,0.5);
y = poisson.pmf(x, mu=parameter, loc = 10);

plt.plot(x,y);

plt.show()


                                                        