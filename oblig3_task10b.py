# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:58:30 2021

@author: alexa
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

weight = float(input("Please type weight: "));

probability = (1 - norm.cdf(weight, 760, 10));


print("It is a probability of " , probability,   " that your inputted weight is heavier than a bread");