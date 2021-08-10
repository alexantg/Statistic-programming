# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:42:27 2021

@author: alexa
"""

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt


x = np.arange(720, 800)
y = norm.pdf(x,760,10);

plt.plot(x,y);

plt.title("Normalfordeling")
plt.ylabel("f(x)");
plt.xlabel("x");

plt.show();
